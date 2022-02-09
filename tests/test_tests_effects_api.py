# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_effect_test(client: AsyncClient) -> None:
    """Test case for get_effect_test

    Get tests effect list
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/tests/{testId}/effects/{effectName}".format(
            testId="testId_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_tests_effects(client: AsyncClient) -> None:
    """Test case for get_tests_effects

    Get tests effects list
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
        "/tests/{testId}/effects/list".format(testId="testId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
