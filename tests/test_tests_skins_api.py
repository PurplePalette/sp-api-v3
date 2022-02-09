# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_skin_test(client: AsyncClient) -> None:
    """Test case for get_skin_test

    Get tests skin
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/tests/{testId}/skins/{skinName}".format(
            testId="testId_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_tests_skins(client: AsyncClient) -> None:
    """Test case for get_tests_skins

    Get tests skin list
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
        "/tests/{testId}/skins/list".format(testId="testId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
