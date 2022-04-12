# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_particle(client: AsyncClient) -> None:
    """Test case for add_particle

    Add a particle
    """

    particle = {
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
        "texture": "hash",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "POST",
        "/particles",
        headers=headers,
        json=particle,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_particle(client: AsyncClient) -> None:
    """Test case for delete_particle

    Delete a particle
    """

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "DELETE",
        "/particles/{particleName}".format(particleName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_particle(client: AsyncClient) -> None:
    """Test case for edit_particle

    Edit a particle
    """
    particle = {
        "title": "b",
        "titleEn": "b",
    }

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "PATCH",
        "/particles/{particleName}".format(particleName="a"),
        headers=headers,
        json=particle,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_particle(client: AsyncClient) -> None:
    """Test case for get_particle

    Get a particle
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/particles/{particleName}".format(particleName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_particle_list(client: AsyncClient) -> None:
    """Test case for get_particle_list

    Get particle list
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
        "/particles/list",
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
