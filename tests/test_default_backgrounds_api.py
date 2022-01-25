# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.background import Background  # noqa: F401
from src.models.get_background_list_response import (
    GetBackgroundListResponse,
)  # noqa: F401
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


def test_add_background(client: TestClient) -> None:
    """Test case for add_background

    Add a background
    """
    background = {
        "image": {"type": "LevelData", "hash": "hash", "url": "url"},
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
        "/backgrounds",
        headers=headers,
        json=background,
    )

    assert response.status_code != 500


def test_delete_background(client: TestClient) -> None:
    """Test case for delete_background

    Delete a background
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(
            backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_background(client: TestClient) -> None:
    """Test case for edit_background

    Edit a background
    """
    background = {
        "image": {"type": "LevelData", "hash": "hash", "url": "url"},
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
        "/backgrounds/{backgroundName}".format(
            backgroundName="background_name_example"
        ),
        headers=headers,
        json=background,
    )

    assert response.status_code != 500


def test_get_background(client: TestClient) -> None:
    """Test case for get_background

    Get a background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/backgrounds/{backgroundName}".format(
            backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_background_list(client: TestClient) -> None:
    """Test case for get_background_list

    Get background list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/backgrounds/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
