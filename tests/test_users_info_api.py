# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.server_info import ServerInfo  # noqa: F401


@pytest.mark.asyncio
async def test_get_user_server_info(client: AsyncClient) -> None:
    """Test case for get_user_server_info

    Get user server info
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}/info".format(userId="userId_example"),
        headers=headers,
    )

    assert response.status_code != 500
