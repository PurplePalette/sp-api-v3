# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_background(client: AsyncClient) -> None:
    """Test case for get_accounts_background

    Get accounts background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/backgrounds/{backgroundName}".format(
            accountKey="account_key_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_accounts_backgrounds(client: AsyncClient) -> None:
    """Test case for get_accounts_backgrounds

    Get accounts background list
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
        "/accounts/{accountKey}/backgrounds/list".format(
            accountKey="account_key_example"
        ),
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
