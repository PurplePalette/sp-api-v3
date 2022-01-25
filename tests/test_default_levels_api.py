# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.level import Level  # noqa: F401


def test_add_level(client: TestClient) -> None:
    """Test case for add_level

    Add a level
    """
    level = {
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "notes": 5637377,
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
        "rating": 81,
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
        "mylists": 7061401,
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
        "genre": ["general"],
        "created_time": 0,
        "bpm": 5962,
        "likes": 2302135,
        "updated_time": 0,
        "author": "author",
        "length": 0,
        "version": 1,
        "user_id": "userId",
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
        "name": "name",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/levels",
        headers=headers,
        json=level,
    )

    assert response.status_code != 500


def test_delete_level(client: TestClient) -> None:
    """Test case for delete_level

    Delete a level
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_level(client: TestClient) -> None:
    """Test case for edit_level

    Edit a level
    """
    level = {
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "notes": 5637377,
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
        "rating": 81,
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
        "mylists": 7061401,
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
        "genre": ["general"],
        "created_time": 0,
        "bpm": 5962,
        "likes": 2302135,
        "updated_time": 0,
        "author": "author",
        "length": 0,
        "version": 1,
        "user_id": "userId",
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
        "name": "name",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
        json=level,
    )

    assert response.status_code != 500


def test_get_level(client: TestClient) -> None:
    """Test case for get_level

    Get a level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/levels/{levelName}".format(levelName="level_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


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

    assert response.status_code != 500
