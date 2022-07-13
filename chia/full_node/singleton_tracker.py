import asyncio
import logging
import time
from typing import Optional, Dict, Tuple, List

from chia.full_node.coin_store import CoinStore
from chia.full_node.singleton_store import SingletonStore, LAUNCHER_PUZZLE_HASH, MAX_REORG_SIZE
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_record import CoinRecord
from chia.util.ints import uint32

log = logging.getLogger(__name__)


class SingletonTracker:
    _singleton_store: SingletonStore
    _coin_store: CoinStore
    fully_started: bool
    _lock: asyncio.Lock

    def __init__(self, coin_store: CoinStore, lock: asyncio.Lock):
        self._coin_store = coin_store
        self.fully_started = False
        self._lock = lock

    async def start1(self, peak_height: uint32) -> None:
        # Call start1 without blockchain lock, then call start2 with blockchain lock
        # This function is safe to call multiple times (without a lock) since such deep reorgs will not happen.
        with self._lock:
            self._singleton_store = SingletonStore(asyncio.Lock())
            self.fully_started = False
            await self._find_singletons_up_to_height(uint32(max(uint32(0), peak_height - 100)))

    async def start2(self, peak_height: uint32) -> None:
        # Call start1 without blockchain lock, then call start2 with blockchain lock.
        # Be careful to only call this when the blockchain is locked.
        with self._lock:
            await self._find_singletons_up_to_height(peak_height)
            self.fully_started = True

    async def new_peak(self, fork_point: uint32, peak_height: uint32) -> None:
        # Be careful to only call this when the blockchain is locked.
        assert self.fully_started
        with self._lock:
            if fork_point < peak_height - 1:
                await self._singleton_store.rollback(fork_point, self._coin_store)
            await self._find_singletons_up_to_height(uint32(peak_height + 1))

    async def get_latest_coin_record_by_launcher_id(self, launcher_id: bytes32) -> Optional[CoinRecord]:
        return await self._singleton_store.get_latest_coin_record_by_launcher_id(launcher_id)

    async def _find_singletons_up_to_height(self, end_height: uint32) -> None:
        # Syncs up the singletons from the current synced height (self._singleton_store.get_peak_height) all the way
        # up to end_height. This includes all singletons where either:
        #   A. Launcher created before start height and launcher spent between start and end height
        #   B. Launcher created and spent between start and end height

        start_t = time.time()
        recent_threshold_height = end_height - (2 * MAX_REORG_SIZE)
        start_height = await self._singleton_store.get_peak_height()
        log.warning(f"Starting singleton sync from {start_height} to {end_height}")

        def confirmed_recently(cr: CoinRecord) -> bool:
            return cr.confirmed_block_index > recent_threshold_height

        if await self._singleton_store.get_peak_height() != uint32(0):
            if end_height <= await self._singleton_store.get_peak_height():
                raise ValueError("End height must occur after the current peak height")

            remaining_launcher_coin_and_curr: List[Tuple[bytes32, CoinRecord]] = [
                (lid, info.latest_state) for lid, info in self._singleton_store.get_all_singletons()
            ]
        else:
            remaining_launcher_coin_and_curr = []

        # The coins_a are the launcher coins that were created before the start height, and spend between start
        # and end height
        unspent_launcher_ids: List[bytes32] = list(self._singleton_store.get_unspent_launcher_ids())
        launcher_coins_a: List[CoinRecord] = [
            cr
            for cr in await self._coin_store.get_coin_records_by_names(
                True, unspent_launcher_ids, end_height=end_height
            )
            if cr.spent
        ]

        launcher_coins_b: List[CoinRecord] = await self._coin_store.get_coin_records_by_puzzle_hash(
            True,
            LAUNCHER_PUZZLE_HASH,
            start_height=start_height,
            end_height=end_height,
        )
        log.warning(f"Found {len(launcher_coins_a)} launcher coins a")
        log.warning(f"Found {len(launcher_coins_b)} launcher coins b")
        chunk_size = 1000

        remaining_launcher_coin_and_curr += [(lc.name, lc) for lc in launcher_coins_a + launcher_coins_b]
        active_launcher_coin_and_curr: List[Tuple[bytes32, CoinRecord]] = remaining_launcher_coin_and_curr[:chunk_size]
        remaining_launcher_coin_and_curr = remaining_launcher_coin_and_curr[chunk_size:]

        # Iterates through all launcher coins, which create potential singletons
        while len(active_launcher_coin_and_curr) > 0:
            new_active_launcher_coin_and_curr: List[Tuple[bytes32, CoinRecord]] = []
            to_lookup = []
            for launcher_id, curr in active_launcher_coin_and_curr:
                curr_name = curr.name
                if curr.spent and curr.spent_block_index <= end_height:
                    to_lookup.append(curr_name)

                if confirmed_recently(curr) or not curr.spent or curr.spent_block_index > end_height:
                    # This is a recent spend (or the last spend), so add it to the list
                    await self._singleton_store.add_state(launcher_id, curr)

            lookup_results: List[CoinRecord] = await self._coin_store.get_coin_records_by_parent_ids(
                True, to_lookup, end_height=uint32(end_height + 1)
            )
            lookup_results_by_parent: Dict[bytes32, List[CoinRecord]] = {}
            for cr in lookup_results:
                parent = cr.coin.parent_coin_info
                if parent not in lookup_results_by_parent:
                    lookup_results_by_parent[parent] = []
                lookup_results_by_parent[parent].append(cr)

            for launcher_id, curr in active_launcher_coin_and_curr:
                assert curr.spent
                children = lookup_results_by_parent.get(curr.name, [])
                if len(children) > 0:
                    # If there is more than one odd child, it's not a valid singleton
                    if len(list(filter(lambda c: c.coin.amount % 2 == 1, children))) != 1:
                        await self._singleton_store.remove_singleton(launcher_id)
                        continue
                    curr = [c for c in children if c.coin.amount % 2 == 1][0]
                    new_active_launcher_coin_and_curr.append((launcher_id, curr))
                elif curr.spent_block_index <= end_height:
                    # This is a spent singleton without any children, so it's no longer valid
                    await self._singleton_store.remove_singleton(launcher_id)
                else:
                    # This is a spent singleton that was spent after the end_height, so we will ignore it
                    pass

            add_new_singletons = chunk_size - len(new_active_launcher_coin_and_curr)
            active_launcher_coin_and_curr = (
                new_active_launcher_coin_and_curr.copy() + remaining_launcher_coin_and_curr[:add_new_singletons]
            )
            remaining_launcher_coin_and_curr = remaining_launcher_coin_and_curr[add_new_singletons:]

        await self._singleton_store.set_peak_height(end_height)
        log.warning(f"Time taken to lookup singletons: {time.time() - start_t} chunk size: {chunk_size}")
