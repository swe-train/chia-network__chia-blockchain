import json
import os
import subprocess
import sysconfig
from typing import Callable, Any
from pathlib import Path
from tests.util.network_protocol_data import *  # noqa: F403

version = "1.0"


tests_dir = Path(__file__).resolve().parent


def get_network_protocol_filename() -> Path:
    return tests_dir / Path(f"protocol_messages_bytes-v{version}.json")


def visit_farmer_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(new_signage_point, "new_signage_point")
    visitor(declare_proof_of_space, "declare_proof_of_space")
    visitor(request_signed_values, "request_signed_values")
    visitor(farming_info, "farming_info")
    visitor(signed_values, "signed_values")


def visit_full_node(visitor: Callable[[Any, str], None]) -> None:
    visitor(new_peak, "new_peak")
    visitor(new_transaction, "new_transaction")
    visitor(request_transaction, "request_transaction")
    visitor(respond_transaction, "respond_transaction")
    visitor(request_proof_of_weight, "request_proof_of_weight")
    visitor(respond_proof_of_weight, "respond_proof_of_weight")
    visitor(request_block, "request_block")
    visitor(reject_block, "reject_block")
    visitor(request_blocks, "request_blocks")
    visitor(respond_blocks, "respond_blocks")
    visitor(reject_blocks, "reject_blocks")
    visitor(respond_block, "respond_block")
    visitor(new_unfinished_block, "new_unfinished_block")
    visitor(request_unfinished_block, "request_unfinished_block")
    visitor(respond_unfinished_block, "respond_unfinished_block")
    visitor(new_signage_point_or_end_of_subslot, "new_signage_point_or_end_of_subslot")
    visitor(request_signage_point_or_end_of_subslot, "request_signage_point_or_end_of_subslot")
    visitor(respond_signage_point, "respond_signage_point")
    visitor(respond_end_of_subslot, "respond_end_of_subslot")
    visitor(request_mempool_transaction, "request_mempool_transaction")
    visitor(new_compact_vdf, "new_compact_vdf")
    visitor(request_compact_vdf, "request_compact_vdf")
    visitor(respond_compact_vdf, "respond_compact_vdf")
    visitor(request_peers, "request_peers")
    visitor(respond_peers, "respond_peers")


def visit_wallet_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(request_puzzle_solution, "request_puzzle_solution")
    visitor(puzzle_solution_response, "puzzle_solution_response")
    visitor(respond_puzzle_solution, "respond_puzzle_solution")
    visitor(reject_puzzle_solution, "reject_puzzle_solution")
    visitor(send_transaction, "send_transaction")
    visitor(transaction_ack, "transaction_ack")
    visitor(new_peak_wallet, "new_peak_wallet")
    visitor(request_block_header, "request_block_header")
    visitor(respond_header_block, "respond_header_block")
    visitor(reject_header_request, "reject_header_request")
    visitor(request_removals, "request_removals")
    visitor(respond_removals, "respond_removals")
    visitor(reject_removals_request, "reject_removals_request")
    visitor(request_additions, "request_additions")
    visitor(respond_additions, "respond_additions")
    visitor(reject_additions, "reject_additions")
    visitor(request_header_blocks, "request_header_blocks")
    visitor(reject_header_blocks, "reject_header_blocks")
    visitor(respond_header_blocks, "respond_header_blocks")
    visitor(coin_state, "coin_state")
    visitor(register_for_ph_updates, "register_for_ph_updates")
    visitor(respond_to_ph_updates, "respond_to_ph_updates")
    visitor(register_for_coin_updates, "register_for_coin_updates")
    visitor(respond_to_coin_updates, "respond_to_coin_updates")
    visitor(coin_state_update, "coin_state_update")
    visitor(request_children, "request_children")
    visitor(respond_children, "respond_children")
    visitor(request_ses_info, "request_ses_info")
    visitor(respond_ses_info, "respond_ses_info")


def visit_harvester_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(pool_difficulty, "pool_difficulty")
    visitor(harvester_handhsake, "harvester_handhsake")
    visitor(new_signage_point_harvester, "new_signage_point_harvester")
    visitor(new_proof_of_space, "new_proof_of_space")
    visitor(request_signatures, "request_signatures")
    visitor(respond_signatures, "respond_signatures")
    visitor(plot, "plot")
    visitor(request_plots, "request_plots")
    visitor(respond_plots, "respond_plots")


def visit_introducer_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(request_peers_introducer, "request_peers_introducer")
    visitor(respond_peers_introducer, "respond_peers_introducer")


def visit_pool_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(authentication_payload, "authentication_payload")
    visitor(get_pool_info_response, "get_pool_info_response")
    visitor(post_partial_payload, "post_partial_payload")
    visitor(post_partial_request, "post_partial_request")
    visitor(post_partial_response, "post_partial_response")
    visitor(get_farmer_response, "get_farmer_response")
    visitor(post_farmer_payload, "post_farmer_payload")
    visitor(post_farmer_request, "post_farmer_request")
    visitor(post_farmer_response, "post_farmer_response")
    visitor(put_farmer_payload, "put_farmer_payload")
    visitor(put_farmer_request, "put_farmer_request")
    visitor(put_farmer_response, "put_farmer_response")
    visitor(error_response, "error_response")


def visit_timelord_protocol(visitor: Callable[[Any, str], None]) -> None:
    visitor(new_peak_timelord, "new_peak_timelord")
    visitor(new_unfinished_block_timelord, "new_unfinished_block_timelord")
    visitor(new_infusion_point_vdf, "new_infusion_point_vdf")
    visitor(new_signage_point_vdf, "new_signage_point_vdf")
    visitor(new_end_of_sub_slot_bundle, "new_end_of_sub_slot_bundle")
    visitor(request_compact_proof_of_time, "request_compact_proof_of_time")
    visitor(respond_compact_proof_of_time, "respond_compact_proof_of_time")


def visit_all_messages(visitor: Callable[[Any, str], None]) -> None:
    visit_farmer_protocol(visitor)
    visit_full_node(visitor)
    visit_wallet_protocol(visitor)
    visit_harvester_protocol(visitor)
    visit_introducer_protocol(visitor)
    visit_pool_protocol(visitor)
    visit_timelord_protocol(visitor)


def get_protocol_bytes() -> str:

    result = {}

    def visitor(obj: Any, name: str) -> None:
        nonlocal result
        result[name] = bytes(obj).hex()

    visit_all_messages(visitor)

    return json.dumps(result, indent=4) + "\n"


def build_protocol_test() -> str:

    result = """# this file is generated by build_network_protocol_files.py

import json

from tests.util.network_protocol_data import *  # noqa: F403
from tests.util.build_network_protocol_files import get_network_protocol_filename


def test_protocol_bytes() -> None:
    input_bytes_hex = json.loads(get_network_protocol_filename().read_text())
    input_bytes = {key: bytes.fromhex(value) for key, value in input_bytes_hex.items()}

"""

    def visitor(obj: Any, name: str) -> None:
        nonlocal result
        result += f"""    message_bytes = input_bytes["{name}"]
    message = type({name}).from_bytes(message_bytes)
    assert message == {name}
    assert bytes(message) == bytes({name})

"""

    visit_all_messages(visitor)

    return result


def get_protocol_json() -> str:
    elements = {}

    def visitor(obj: Any, name: str) -> None:
        elements[name] = obj.to_json_dict()

    visit_all_messages(visitor)

    return json.dumps(elements, indent=4) + "\n"


def build_data() -> str:

    result = """# this file is generated by build_network_protocol_files.py

from tests.util.network_protocol_data import *  # noqa: F403

name_to_instance = {
"""
    counter = 0

    def visitor(obj: Any, name: str) -> None:
        nonlocal result
        nonlocal counter
        result += f'    "{name}": {name},\n'
        counter += 1

    visit_all_messages(visitor)

    result += """
}
"""

    return result


if __name__ == "__main__":
    name_to_function = {
        os.fspath(get_network_protocol_filename()): get_protocol_bytes,
        "test_network_protocol_files.py": build_protocol_test,
        "network_protocol_messages.json": get_protocol_json,
        "network_protocol_data2.py": build_data,
    }

    scripts_path = Path(sysconfig.get_path("scripts"))

    for name, function in name_to_function.items():
        path = tests_dir.joinpath(name)
        path.write_text(function())
        if path.suffix == ".py":
            # black seems to have trouble when run as a module so not using `python -m black`
            subprocess.run(
                [scripts_path.joinpath("black"), os.fspath(path.relative_to(tests_dir))],
                check=True,
                cwd=tests_dir,
            )
