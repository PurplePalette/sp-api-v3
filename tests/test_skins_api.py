# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401
from src.models.skin import Skin  # noqa: F401


def test_add_skin(client: TestClient) -> None:
    """Test case for add_skin

    Add skin
    """
    skin = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
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
        "/skins",
        headers=headers,
        json=skin,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_delete_skin(client: TestClient) -> None:
    """Test case for delete_skin

    Delete skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "DELETE",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_edit_skin(client: TestClient) -> None:
    """Test case for edit_skin

    Edit skin
    """
    skin = {
        "updated_time": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
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
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
        json=skin,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_skin(client: TestClient) -> None:
    """Test case for get_skin

    Get skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/skins/{skinName}".format(skinName="skin_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_skin_list(client: TestClient) -> None:
    """Test case for get_skin_list

    Get skin list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/skins/list",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
