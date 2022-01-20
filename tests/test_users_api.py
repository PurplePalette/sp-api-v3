# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_background_list_response import (
    GetBackgroundListResponse,
)  # noqa: F401
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
from src.models.get_user_list_response import GetUserListResponse  # noqa: F401
from src.models.server_info import ServerInfo  # noqa: F401
from src.models.user import User  # noqa: F401


def test_delete_user(client: TestClient) -> None:
    """Test case for delete_user

    Delete user
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "DELETE",
        "/users/{userId}".format(userId="user_id_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_edit_user(client: TestClient) -> None:
    """Test case for edit_user

    Edit user
    """
    user = {
        "updated_time": 0,
        "is_deleted": 0,
        "total_played": 563737,
        "total_fumen": 146581,
        "created_time": 0,
        "description": "description",
        "test_id": "htcckfcn",
        "is_admin": 0,
        "total_likes": 596213,
        "user_id": "gz6xQrm79IN4BiQag78sQqYWYlC3",
    }

    headers: Dict[str, str] = {}
    response = client.request(
        "PATCH",
        "/users/{userId}".format(userId="user_id_example"),
        headers=headers,
        json=user,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_user(client: TestClient) -> None:
    """Test case for get_user

    Get user
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}".format(userId="user_id_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_user_list(client: TestClient) -> None:
    """Test case for get_user_list

    Get user list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/list",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_user_server_info(client: TestClient) -> None:
    """Test case for get_user_server_info

    Get user server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/info".format(userId="user_id_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_background(client: TestClient) -> None:
    """Test case for get_users_background

    Get users background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/backgrounds/{backgroundName}".format(
            userId="user_id_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_backgrounds(client: TestClient) -> None:
    """Test case for get_users_backgrounds

    Get backgrounds for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/backgrounds/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_effect(client: TestClient) -> None:
    """Test case for get_users_effect

    Get users effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/effects/{effectName}".format(
            userId="user_id_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_effects(client: TestClient) -> None:
    """Test case for get_users_effects

    Get effects for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/effects/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_engine(client: TestClient) -> None:
    """Test case for get_users_engine

    Get users engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/engines/{engineName}".format(
            userId="user_id_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_engines(client: TestClient) -> None:
    """Test case for get_users_engines

    Get engines for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/engines/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_level(client: TestClient) -> None:
    """Test case for get_users_level

    Get users level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/levels/{levelName}".format(
            userId="user_id_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_levels(client: TestClient) -> None:
    """Test case for get_users_levels

    Get levels for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/levels/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


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

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_particles(client: TestClient) -> None:
    """Test case for get_users_particles

    Get particles for test
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

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_skin(client: TestClient) -> None:
    """Test case for get_users_skin

    Get users skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/skins/{skinName}".format(
            userId="user_id_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_users_skins(client: TestClient) -> None:
    """Test case for get_users_skins

    Get skins for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/skins/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
