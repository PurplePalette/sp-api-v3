# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401
from src.models.skin import Skin  # noqa: F401


@pytest.mark.asyncio
async def test_add_skin(client: AsyncClient) -> None:
    """Test case for add_skin

    Add a skin
    """
    skin = {
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
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "POST",
        "/skins",
        headers=headers,
        json=skin,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_skin(client: AsyncClient) -> None:
    """Test case for delete_skin

    Delete a skin
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_skin(client: AsyncClient) -> None:
    """Test case for edit_skin

    Edit a skin
    """
    skin = {
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
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
        json=skin,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_skin(client: AsyncClient) -> None:
    """Test case for get_skin

    Get a skin
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_skin_list(client: AsyncClient) -> None:
    """Test case for get_skin_list

    Get skin list
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
        "/skins/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
