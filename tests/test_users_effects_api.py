# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
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
            userId="userId_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_users_effects(client: TestClient) -> None:
    """Test case for get_users_effects

    Get users effect list
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
        "/users/{userId}/effects/list".format(userId="userId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
