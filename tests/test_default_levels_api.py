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
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "notes": 5637377,
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "use_background": {
            "item": {
                "descriptionEn": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "rating": 8,
        "use_skin": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "mylists": 7061401,
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "background": {
                "descriptionEn": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "subtitle": "subtitle",
            "effect": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "name": "name",
            "createdTime": 0,
            "particle": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "authorEn": "authorEn",
        },
        "artists": "artists",
        "use_particle": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "genre": ["general"],
        "createdTime": 0,
        "bpm": 5962,
        "likes": 2302135,
        "descriptionEn": "No description",
        "updatedTime": 0,
        "author": "author",
        "length": 0,
        "artistsEn": "artistsEn",
        "version": 1,
        "userId": "userId",
        "titleEn": "titleEn",
        "use_effect": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "name": "name",
        "authorEn": "authorEn",
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

    assert response.status_code != 500


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
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_level(client: AsyncClient) -> None:
    """Test case for edit_level

    Edit a level
    """
    level = {
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "notes": 5637377,
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "use_background": {
            "item": {
                "descriptionEn": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "rating": 8,
        "use_skin": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "mylists": 7061401,
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "background": {
                "descriptionEn": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "subtitle": "subtitle",
            "effect": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "name": "name",
            "createdTime": 0,
            "particle": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "authorEn": "authorEn",
        },
        "artists": "artists",
        "use_particle": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "genre": ["general"],
        "createdTime": 0,
        "bpm": 5962,
        "likes": 2302135,
        "descriptionEn": "No description",
        "updatedTime": 0,
        "author": "author",
        "length": 0,
        "artistsEn": "artistsEn",
        "version": 1,
        "userId": "userId",
        "titleEn": "titleEn",
        "use_effect": {
            "item": {
                "descriptionEn": "No description",
                "updatedTime": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitleEn": "subtitleEn",
                "userId": "userId",
                "titleEn": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "createdTime": 0,
                "authorEn": "authorEn",
            },
            "use_default": 1,
        },
        "name": "name",
        "authorEn": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
        json=level,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_level(client: AsyncClient) -> None:
    """Test case for get_level

    Get a level
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


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

    assert response.status_code != 500
