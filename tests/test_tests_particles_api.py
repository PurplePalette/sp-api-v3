# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401


def test_get_particle_test(client: TestClient) -> None:
    """Test case for get_particle_test

    Get tests particle
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/particles/{particleName}".format(
            testId="test_id_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_particles(client: TestClient) -> None:
    """Test case for get_tests_particles

    Get tests particle list
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
    response = client.request(
        "GET",
        "/tests/{testId}/particles/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
