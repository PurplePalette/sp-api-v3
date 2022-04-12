# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.effect import Effect  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


@pytest.mark.asyncio
async def test_add_effect(client: AsyncClient) -> None:
    """Test case for add_effect

    Add an effect
    """
    effect = {
        "title": "title",
        "titleEn": "titleEn",
        "description": "No description",
        "descriptionEn": "No description",
        "subtitle": "subtitle",
        "subtitleEn": "subtitleEn",
        "author": "author",
        "authorEn": "authorEn",
        "thumbnail": "hash",
        "data": "hash",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "POST",
        "/effects",
        headers=headers,
        json=effect,
    )
    print(response.json())
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_effect(client: AsyncClient) -> None:
    """Test case for delete_effect

    Delete an effect
    """

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "DELETE",
        "/effects/{effectName}".format(effectName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_effect(client: AsyncClient) -> None:
    """Test case for edit_effect

    Edit an effect
    """
    effect = {
        "title": "b",
        "titleEn": "b",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "PATCH",
        "/effects/{effectName}".format(effectName="a"),
        headers=headers,
        json=effect,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_effect(client: AsyncClient) -> None:
    """Test case for get_effect

    Get an effect
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/effects/{effectName}".format(effectName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_effect_list(client: AsyncClient) -> None:
    """Test case for get_effect_list

    Get effect list
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
        "/effects/list",
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
