# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_skin(client: AsyncClient) -> None:
    """Test case for get_accounts_skin

    Get accounts skin
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/skins/{skinName}".format(
            accountKey="account_key_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_accounts_skins(client: AsyncClient) -> None:
    """Test case for get_accounts_skins

    Get accounts skin list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "0",
        "order": "0",
        "status": "0",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/skins/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
