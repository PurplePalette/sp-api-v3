# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.engine import Engine  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


def test_add_engine(client: TestClient) -> None:
    """Test case for add_engine

    Add an engine
    """
    engine = {
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
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/engines",
        headers=headers,
        json=engine,
    )

    assert response.status_code != 500


def test_delete_engine(client: TestClient) -> None:
    """Test case for delete_engine

    Delete an engine
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/engines/{engineName}".format(engineName="engine_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_engine(client: TestClient) -> None:
    """Test case for edit_engine

    Edit an engine
    """
    engine = {
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
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/engines/{engineName}".format(engineName="engine_name_example"),
        headers=headers,
        json=engine,
    )

    assert response.status_code != 500


def test_get_engine(client: TestClient) -> None:
    """Test case for get_engine

    Get an engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/engines/{engineName}".format(engineName="engine_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_engine_list(client: TestClient) -> None:
    """Test case for get_engine_list

    Get engine list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/engines/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
