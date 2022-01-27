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
                "description_en": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "rating": 8,
        "use_skin": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "mylists": 7061401,
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "description_en": "No description",
            "updated_time": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitle_en": "subtitleEn",
            "user_id": "userId",
            "title_en": "titleEn",
            "background": {
                "description_en": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "subtitle": "subtitle",
            "effect": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "name": "name",
            "created_time": 0,
            "particle": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "author_en": "authorEn",
        },
        "artists": "artists",
        "use_particle": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "genre": ["general"],
        "created_time": 0,
        "bpm": 5962,
        "likes": 2302135,
        "description_en": "No description",
        "updated_time": 0,
        "author": "author",
        "length": 0,
        "artists_en": "artistsEn",
        "version": 1,
        "user_id": "userId",
        "title_en": "titleEn",
        "use_effect": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "name": "name",
        "author_en": "authorEn",
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
                "description_en": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "rating": 8,
        "use_skin": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "mylists": 7061401,
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "engine": {
            "description_en": "No description",
            "updated_time": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "skin": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitle_en": "subtitleEn",
            "user_id": "userId",
            "title_en": "titleEn",
            "background": {
                "description_en": "No description",
                "image": {"type": "LevelData", "hash": "hash", "url": "url"},
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "subtitle": "subtitle",
            "effect": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "name": "name",
            "created_time": 0,
            "particle": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "author_en": "authorEn",
        },
        "artists": "artists",
        "use_particle": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "genre": ["general"],
        "created_time": 0,
        "bpm": 5962,
        "likes": 2302135,
        "description_en": "No description",
        "updated_time": 0,
        "author": "author",
        "length": 0,
        "artists_en": "artistsEn",
        "version": 1,
        "user_id": "userId",
        "title_en": "titleEn",
        "use_effect": {
            "item": {
                "description_en": "No description",
                "updated_time": 0,
                "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
                "data": {"type": "LevelData", "hash": "hash", "url": "url"},
                "author": "author",
                "description": "No description",
                "title": "title",
                "version": 1,
                "subtitle_en": "subtitleEn",
                "user_id": "userId",
                "title_en": "titleEn",
                "subtitle": "subtitle",
                "name": "name",
                "created_time": 0,
                "author_en": "authorEn",
            },
            "use_default": 1,
        },
        "name": "name",
        "author_en": "authorEn",
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
        "/levels/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
