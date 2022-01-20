# coding: utf-8

from typing import Dict
from fastapi.testclient import TestClient


from src.models.effect import Effect  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


def test_add_effect(client: TestClient) -> None:
    """Test case for add_effect

    Add effect
    """
    effect = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
    }

    headers: Dict[str, str] = {}
    response = client.request(
        "POST",
        "/effects",
        headers=headers,
        json=effect,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_delete_effect(client: TestClient) -> None:
    """Test case for delete_effect

    Delete effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "DELETE",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_edit_effect(client: TestClient) -> None:
    """Test case for edit_effect

    Edit effect
    """
    effect = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
    }

    headers: Dict[str, str] = {}
    response = client.request(
        "PATCH",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
        json=effect,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_effect(client: TestClient) -> None:
    """Test case for get_effect

    Get effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_effect_list(client: TestClient) -> None:
    """Test case for get_effect_list

    Get effect list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/effects/list",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
