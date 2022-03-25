# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_users_particle(client: AsyncClient) -> None:
    """Test case for get_users_particle

    Get users particle
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}/particles/{particleName}".format(
            userId="userId_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_users_particles(client: AsyncClient) -> None:
    """Test case for get_users_particles

    Get users particle list
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
        "/users/{userId}/particles/list".format(userId="userId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
