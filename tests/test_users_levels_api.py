# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_users_level(client: AsyncClient) -> None:
    """Test case for get_users_level

    Get users level
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}/levels/{levelName}".format(
            userId="userId_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_users_levels(client: AsyncClient) -> None:
    """Test case for get_users_levels

    Get users level list
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
        "/users/{userId}/levels/list".format(userId="userId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
