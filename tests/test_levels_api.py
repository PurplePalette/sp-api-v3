# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.level import Level  # noqa: F401


def test_add_level(client: TestClient) -> None:
    """Test case for add_level

    Add level
    """
    level = {
        "updated_time": 0,
        "notes": 6027456,
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "use_background": {
            "item": {
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
            },
            "use_default": 1,
        },
        "author": "author",
        "rating": 81,
        "length": 0,
        "use_skin": {
            "item": {
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
            },
            "use_default": 1,
        },
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "updated_time": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
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
            },
            "description": "description",
            "title": "title",
            "version": 1,
            "user_id": "userId",
            "background": {
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
            },
            "subtitle": "subtitle",
            "effect": {
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
            },
            "name": "name",
            "created_time": 0,
            "particle": {
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
            },
        },
        "artists": "artists",
        "use_effect": {
            "item": {
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
            },
            "use_default": 1,
        },
        "use_particle": {
            "item": {
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
            },
            "use_default": 1,
        },
        "name": "name",
        "genre": "general",
        "created_time": 0,
    }

    headers: Dict[str, str] = {}
    response = client.request(
        "POST",
        "/levels",
        headers=headers,
        json=level,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_delete_level(client: TestClient) -> None:
    """Test case for delete_level

    Delete a level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "DELETE",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_edit_level(client: TestClient) -> None:
    """Test case for edit_level

    Edit level
    """
    level = {
        "updated_time": 0,
        "notes": 6027456,
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "use_background": {
            "item": {
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
            },
            "use_default": 1,
        },
        "author": "author",
        "rating": 81,
        "length": 0,
        "use_skin": {
            "item": {
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
            },
            "use_default": 1,
        },
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description": "description",
        "title": "title",
        "version": 1,
        "user_id": "userId",
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "updated_time": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
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
            },
            "description": "description",
            "title": "title",
            "version": 1,
            "user_id": "userId",
            "background": {
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
            },
            "subtitle": "subtitle",
            "effect": {
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
            },
            "name": "name",
            "created_time": 0,
            "particle": {
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
            },
        },
        "artists": "artists",
        "use_effect": {
            "item": {
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
            },
            "use_default": 1,
        },
        "use_particle": {
            "item": {
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
            },
            "use_default": 1,
        },
        "name": "name",
        "genre": "general",
        "created_time": 0,
    }

    headers: Dict[str, str] = {}
    response = client.request(
        "PATCH",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
        json=level,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_level(client: TestClient) -> None:
    """Test case for get_level

    Get level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_level_list(client: TestClient) -> None:
    """Test case for get_level_list

    Get level list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/levels/list",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
