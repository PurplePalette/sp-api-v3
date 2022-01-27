# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.engine import Engine  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


def test_add_engine(client: TestClient) -> None:
    """Test case for add_engine

    Add an engine
    """
    engine = {
        "descriptionEn": "No description",
        "updatedTime": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "skin": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "description": "No description",
        "title": "title",
        "version": 1,
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "titleEn": "titleEn",
        "background": {
            "descriptionEn": "No description",
            "image": {"type": "LevelData", "hash": "hash", "url": "url"},
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "subtitle": "subtitle",
        "effect": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "name": "name",
        "createdTime": 0,
        "particle": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "authorEn": "authorEn",
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
        "descriptionEn": "No description",
        "updatedTime": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "skin": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "description": "No description",
        "title": "title",
        "version": 1,
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "titleEn": "titleEn",
        "background": {
            "descriptionEn": "No description",
            "image": {"type": "LevelData", "hash": "hash", "url": "url"},
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "subtitle": "subtitle",
        "effect": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "name": "name",
        "createdTime": 0,
        "particle": {
            "descriptionEn": "No description",
            "updatedTime": 0,
            "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
            "data": {"type": "LevelData", "hash": "hash", "url": "url"},
            "author": "author",
            "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
            "description": "No description",
            "title": "title",
            "version": 1,
            "subtitleEn": "subtitleEn",
            "userId": "userId",
            "titleEn": "titleEn",
            "subtitle": "subtitle",
            "name": "name",
            "createdTime": 0,
            "authorEn": "authorEn",
        },
        "authorEn": "authorEn",
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
        "/engines/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
