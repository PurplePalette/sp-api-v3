# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.server_info import ServerInfo  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_server_info(client: AsyncClient) -> None:
    """Test case for get_accounts_server_info

    Get account server info
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/info".format(accountKey="account_key_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500
