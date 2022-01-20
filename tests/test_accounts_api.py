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


def test_decrease_rating(client: TestClient) -> None:
    """Test case for decrease_rating

    Rate level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/rating_decrease_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_favorite_level(client: TestClient) -> None:
    """Test case for favorite_level

    Add level to user favorite
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/favorite_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_announce(client: TestClient) -> None:
    """Test case for get_account_announce

    Get announce
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/announce_{announceName}".format(
            accountKey="account_key_example", announceName="announce_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_announce_list(client: TestClient) -> None:
    """Test case for get_account_announce_list

    Get announce list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/announce".format(
            accountKey="account_key_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_mylist(client: TestClient) -> None:
    """Test case for get_account_mylist

    Get mylist
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/mylist".format(accountKey="account_key_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_random(client: TestClient) -> None:
    """Test case for get_account_random

    Get random
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/random".format(accountKey="account_key_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_background(client: TestClient) -> None:
    """Test case for get_accounts_background

    Get accounts background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/backgrounds/{backgroundName}".format(
            accountKey="account_key_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_backgrounds(client: TestClient) -> None:
    """Test case for get_accounts_backgrounds

    Get backgrounds for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/backgrounds/list".format(
            accountKey="account_key_example"
        ),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_effect(client: TestClient) -> None:
    """Test case for get_accounts_effect

    Get accounts effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/effects/{effectName}".format(
            accountKey="account_key_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_effects(client: TestClient) -> None:
    """Test case for get_accounts_effects

    Get effects for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/effects/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_engine(client: TestClient) -> None:
    """Test case for get_accounts_engine

    Get accounts engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/engines/{engineName}".format(
            accountKey="account_key_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_engines(client: TestClient) -> None:
    """Test case for get_accounts_engines

    Get engines for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/engines/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_level(client: TestClient) -> None:
    """Test case for get_accounts_level

    Get accounts level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_levels(client: TestClient) -> None:
    """Test case for get_accounts_levels

    Get levels for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


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

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_particles(client: TestClient) -> None:
    """Test case for get_accounts_particles

    Get particles for test
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

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_server_info(client: TestClient) -> None:
    """Test case for get_accounts_server_info

    Get user server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/info".format(accountKey="account_key_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_skin(client: TestClient) -> None:
    """Test case for get_accounts_skin

    Get accounts skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/skins/{skinName}".format(
            accountKey="account_key_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_accounts_skins(client: TestClient) -> None:
    """Test case for get_accounts_skins

    Get skins for test
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/skins/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_flick_level(client: TestClient) -> None:
    """Test case for get_flick_level

    Get flick level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/flick_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_increase_rating(client: TestClient) -> None:
    """Test case for increase_rating

    Rate level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/rating_increase_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_rate_level(client: TestClient) -> None:
    """Test case for rate_level

    Rate level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/up_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_unfavorite_level(client: TestClient) -> None:
    """Test case for unfavorite_level

    Add level to user favorite
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/unfavorite_{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500
