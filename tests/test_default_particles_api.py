# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401
from src.models.particle import Particle  # noqa: F401


@pytest.mark.asyncio
async def test_add_particle(client: AsyncClient) -> None:
    """Test case for add_particle

    Add a particle
    """
    particle = {
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
        "/particles",
        headers=headers,
        json=particle,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_particle(client: AsyncClient) -> None:
    """Test case for delete_particle

    Delete a particle
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_particle(client: AsyncClient) -> None:
    """Test case for edit_particle

    Edit a particle
    """
    particle = {
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
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
        json=particle,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_particle(client: AsyncClient) -> None:
    """Test case for get_particle

    Get a particle
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_particle_list(client: AsyncClient) -> None:
    """Test case for get_particle_list

    Get particle list
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
        "/particles/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
