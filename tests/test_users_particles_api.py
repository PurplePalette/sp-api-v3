# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401


def test_get_users_particle(client: TestClient) -> None:
    """Test case for get_users_particle

    Get users particle
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/particles/{particleName}".format(
            userId="user_id_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_users_particles(client: TestClient) -> None:
    """Test case for get_users_particles

    Get users particle list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/particles/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
