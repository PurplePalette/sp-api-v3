# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.server_info import ServerInfo  # noqa: F401


@pytest.mark.asyncio
async def test_get_server_info(client: AsyncClient) -> None:
    """Test case for get_server_info

    Get default server info
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/info",
        headers=headers,
    )

    assert response.status_code != 500
