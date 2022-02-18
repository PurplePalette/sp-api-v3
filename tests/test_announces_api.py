# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.database.db import get_db  # noqa: F401
from src.models.announce import Announce  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


@pytest.mark.asyncio
async def test_add_announce(client: AsyncClient) -> None:
    """Test case for add_announce

    Add announce
    """
    announce = {
        "preview": "hash",
        "descriptionEn": "No description",
        "updatedTime": 0,
        "author": "author",
        "rating": 8,
        "description": "No description",
        "bgm": "hash",
        "title": "title",
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "cover": "hash",
        "public": 0,
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
        "/announces",
        headers=headers,
        json=announce,
    )
    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_announce(client: AsyncClient) -> None:
    """Test case for delete_announce

    Delete announce
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/announces/{announceName}".format(announceName="name"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_announce(client: AsyncClient) -> None:
    """Test case for edit_announce

    Edit announce
    """
    announce = {
        "preview": "url",
        "descriptionEn": "No description",
        "updatedTime": 0,
        "author": "author",
        "rating": 8,
        "description": "No description",
        "bgm": "hash",
        "title": "title",
        "subtitleEn": "subtitleEn",
        "cover": "hash",
        "public": 0,
        "titleEn": "titleEn",
        "subtitle": "hello_world",
        "name": "name",
        "createdTime": 0,
        "authorEn": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/announces/{announceName}".format(announceName="name"),
        headers=headers,
        json=announce,
    )
    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_default_announce(client: AsyncClient) -> None:
    """Test case for get_default_announce

    Get announce
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/announces/{announceName}".format(announceName="WELCOME"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_default_announces(client: AsyncClient) -> None:
    """Test case for get_default_announces

    Get announce list
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/announces/list",
        headers=headers,
    )

    assert response.status_code != 500
