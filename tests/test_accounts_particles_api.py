# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401


def test_get_accounts_particle(client: TestClient) -> None:
    """Test case for get_accounts_particle

    Get accounts particle
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/particles/{particleName}".format(
            accountKey="account_key_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_accounts_particles(client: TestClient) -> None:
    """Test case for get_accounts_particles

    Get accounts particle list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/particles/list".format(
            accountKey="account_key_example"
        ),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
