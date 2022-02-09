# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_effect(client: AsyncClient) -> None:
    """Test case for get_accounts_effect

    Get accounts effect
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/effects/{effectName}".format(
            accountKey="account_key_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_accounts_effects(client: AsyncClient) -> None:
    """Test case for get_accounts_effects

    Get accounts effect list
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
        "/accounts/{accountKey}/effects/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
