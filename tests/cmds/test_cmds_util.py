from __future__ import annotations

import pytest

from chia.cmds.cmds_util import get_any_service_client
from chia.rpc.rpc_client import RpcClient
from tests.util.misc import RecordingWebServer


@pytest.mark.anyio
async def test_get_any_service_client_works_without_ssl(recording_web_server: RecordingWebServer) -> None:
    expected_result = {"success": True, "keepy": "uppy"}

    async with get_any_service_client(
        client_type=RpcClient,
        rpc_port=recording_web_server.web_server.listen_port,
        use_ssl=False,
    ) as [rpc_client, _]:
        result = await rpc_client.fetch(path="", request_json={"response": expected_result})

    assert result == expected_result
