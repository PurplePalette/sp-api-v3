# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401
from src.models.server_info import ServerInfo  # noqa: F401


def test_get_background_test(client: TestClient) -> None:
    """Test case for get_background_test

    Get testing background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/backgrounds/{backgroundName}".format(
            testId="test_id_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_effect_test(client: TestClient) -> None:
    """Test case for get_effect_test

    Get testing effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/effects/{effectName}".format(
            testId="test_id_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_engine_test(client: TestClient) -> None:
    """Test case for get_engine_test

    Get testing engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/engines/{engineName}".format(
            testId="test_id_example", engineName="engine_name_example"
        ),
        headers=headers,
    )
    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_level_test(client: TestClient) -> None:
    """Test case for get_level_test

    Get testing level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/levels/{levelName}".format(
            testId="test_id_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_particle_test(client: TestClient) -> None:
    """Test case for get_particle_test

    Get testing particle
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/particles/{particleName}".format(
            testId="test_id_example", particleName="particle_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_skin_test(client: TestClient) -> None:
    """Test case for get_skin_test

    Get testing skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/skins/{skinName}".format(
            testId="test_id_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_test_server_info(client: TestClient) -> None:
    """Test case for get_test_server_info

    Get user server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/info".format(testId="test_id_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_backgrounds(client: TestClient) -> None:
    """Test case for get_tests_backgrounds

    Get backgrounds for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/backgrounds/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_effects(client: TestClient) -> None:
    """Test case for get_tests_effects

    Get effects for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/effects/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_engines(client: TestClient) -> None:
    """Test case for get_tests_engines

    Get engines for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/engines/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_levels(client: TestClient) -> None:
    """Test case for get_tests_levels

    Get levels for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/levels/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_particles(client: TestClient) -> None:
    """Test case for get_tests_particles

    Get particles for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/particles/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_tests_skins(client: TestClient) -> None:
    """Test case for get_tests_skins

    Get skins for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/skins/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500
