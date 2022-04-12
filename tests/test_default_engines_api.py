# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.engine import Engine  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


@pytest.mark.asyncio
async def test_add_engine(client: AsyncClient) -> None:
    """Test case for add_engine

    Add an engine
    """
    engine = {
        "title": "title",
        "titleEn": "titleEn",
        "author": "author",
        "authorEn": "authorEn",
        "subtitle": "subtitle",
        "subtitleEn": "subtitleEn",
        "description": "No description",
        "descriptionEn": "No description",
        "thumbnail": "hash",
        "data": "hash",
        "configuration": "hash",
        "skin": "a",
        "background": "a",
        "particle": "a",
        "effect": "a",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "POST",
        "/engines",
        headers=headers,
        json=engine,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_engine(client: AsyncClient) -> None:
    """Test case for delete_engine

    Delete an engine
    """

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "DELETE",
        "/engines/{engineName}".format(engineName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_engine(client: AsyncClient) -> None:
    """Test case for edit_engine

    Edit an engine
    """
    engine = {
        "title": "b",
        "titleEn": "b",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "PATCH",
        "/engines/{engineName}".format(engineName="a"),
        headers=headers,
        json=engine,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_engine(client: AsyncClient) -> None:
    """Test case for get_engine

    Get an engine
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/engines/{engineName}".format(engineName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_engine_list(client: AsyncClient) -> None:
    """Test case for get_engine_list

    Get engine list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "0",
        "order": "0",
        "status": "0",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/engines/list",
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
