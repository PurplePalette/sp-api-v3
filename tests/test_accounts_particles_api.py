# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_accounts_particle(client: AsyncClient) -> None:
    """Test case for get_accounts_particle

    Get accounts particle
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/accounts/{accountKey}/particles/{particleName}".format(
            accountKey="account_key_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_accounts_particles(client: AsyncClient) -> None:
    """Test case for get_accounts_particles

    Get accounts particle list
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
        "/accounts/{accountKey}/particles/list".format(
            accountKey="account_key_example"
        ),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
