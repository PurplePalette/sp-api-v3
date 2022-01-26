# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.effect import Effect  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


def test_add_effect(client: TestClient) -> None:
    """Test case for add_effect

    Add an effect
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

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/effects",
        headers=headers,
        json=effect,
    )

    assert response.status_code != 500


def test_delete_effect(client: TestClient) -> None:
    """Test case for delete_effect

    Delete an effect
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_effect(client: TestClient) -> None:
    """Test case for edit_effect

    Edit an effect
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

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
        json=effect,
    )

    assert response.status_code != 500


def test_get_effect(client: TestClient) -> None:
    """Test case for get_effect

    Get an effect
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/effects/{effectName}".format(effectName="effect_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_effect_list(client: TestClient) -> None:
    """Test case for get_effect_list

    Get effect list
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
        "/effects/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
