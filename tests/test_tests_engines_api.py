# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_engine_test(client: AsyncClient) -> None:
    """Test case for get_engine_test

    Get tests engine
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/tests/{testId}/engines/{engineName}".format(
            testId="testId_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_tests_engines(client: AsyncClient) -> None:
    """Test case for get_tests_engines

    Get tests engine list
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
        "/tests/{testId}/engines/list".format(testId="testId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
