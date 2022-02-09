# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_level(client: AsyncClient) -> None:
    """Test case for get_accounts_level

    Get accounts level
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/levels/{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_accounts_levels(client: AsyncClient) -> None:
    """Test case for get_accounts_levels

    Get accounts level list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "updated_time",
        "order": "desc",
        "status": "any",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/levels/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
