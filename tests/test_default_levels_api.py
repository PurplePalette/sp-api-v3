# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.level import Level  # noqa: F401


@pytest.mark.asyncio
async def test_add_level(client: AsyncClient) -> None:
    """Test case for add_level

    Add a level
    """
    level = {
        "title": "title",
        "titleEn": "titleEn",
        "author": "author",
        "authorEn": "authorEn",
        "artists": "artists",
        "artistsEn": "artistsEn",
        "description": "No description",
        "descriptionEn": "No description",
        "genre": "general",
        "engine": "a",
        "background": None,
        "skin": None,
        "particle": None,
        "effect": None,
        "cover": "hash",
        "bgm": "hash",
        "data": "hash",
        "preview": "hash",
        "length": 0,
        "bpm": 555,
        "notes": 2000,
        "rating": 8,
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "POST",
        "/levels",
        headers=headers,
        json=level,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_level(client: AsyncClient) -> None:
    """Test case for delete_level

    Delete a level
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/levels/{levelName}".format(levelName="botorushippunotabi"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_level(client: AsyncClient) -> None:
    """Test case for edit_level

    Edit a level
    """
    level = {
        "title": "b",
        "titleEn": "b",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/levels/{levelName}".format(levelName="botorushippunotabi"),
        headers=headers,
        json=level,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_level(client: AsyncClient) -> None:
    """Test case for get_level

    Get a level
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/{levelName}".format(levelName="botorushippunotabi"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_level_list(client: AsyncClient) -> None:
    """Test case for get_level_list

    Get level list
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
        "/levels/list",
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
