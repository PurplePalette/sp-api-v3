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
        "name": "name",
        "title": "title",
        "titleEn": "titleEn",
        "subtitle": "subtitle",
        "subtitleEn": "subtitleEn",
        "author": "author",
        "authorEn": "authorEn",
        "description": "No description",
        "descriptionEn": "No description",
        "rating": 10,
        "cover": "hash",
        "bgm": "hash",
        "preview": "hash",
    }

    headers = {
        "Authorization": "Bearer admin",
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
        "Authorization": "Bearer admin",
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
        "subtitle": "ハローワールド",
        "subtitleEn": "hello world",
    }

    headers = {
        "Authorization": "Bearer admin",
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
