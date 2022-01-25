# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


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

    assert response.status_code != 500


def test_get_users_effects(client: TestClient) -> None:
    """Test case for get_users_effects

    Get users effect list
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

    assert response.status_code != 500
