# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.server_info import ServerInfo  # noqa: F401


@pytest.mark.asyncio
async def test_get_test_server_info(client: AsyncClient) -> None:
    """Test case for get_test_server_info

    Get test server info
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/tests/{testId}/info".format(testId="testId_example"),
        headers=headers,
    )

    assert response.status_code != 500
