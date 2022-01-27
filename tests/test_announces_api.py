# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.announce import Announce  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


def test_add_announce(client: TestClient) -> None:
    """Test case for add_announce

    Add announce
    """
    announce = {
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description_en": "No description",
        "updated_time": 0,
        "author": "author",
        "rating": 8,
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "subtitle_en": "subtitleEn",
        "user_id": "userId",
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "title_en": "titleEn",
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "author_en": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/announces",
        headers=headers,
        json=announce,
    )
    assert response.status_code != 500


def test_delete_announce(client: TestClient) -> None:
    """Test case for delete_announce

    Delete announce
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/announces/{announceName}".format(announceName="announceName"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_announce(client: TestClient) -> None:
    """Test case for edit_announce

    Edit announce
    """
    announce = {
        "preview": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description_en": "No description",
        "updated_time": 0,
        "author": "author",
        "rating": 8,
        "description": "No description",
        "bgm": {"type": "LevelData", "hash": "hash", "url": "url"},
        "title": "title",
        "subtitle_en": "subtitleEn",
        "user_id": "userId",
        "cover": {"type": "LevelData", "hash": "hash", "url": "url"},
        "public": 0,
        "title_en": "titleEn",
        "subtitle": "subtitle",
        "name": "name",
        "created_time": 0,
        "author_en": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/announces/{announceName}".format(announceName="announceName"),
        headers=headers,
        json=announce,
    )
    assert response.status_code != 500


def test_get_default_announce(client: TestClient) -> None:
    """Test case for get_default_announce

    Get announce
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/announces/{announceName}".format(announceName="announce_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_default_announces(client: TestClient) -> None:
    """Test case for get_default_announces

    Get announce list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/announces/list",
        headers=headers,
    )

    assert response.status_code != 500


def test_get_pickup_list(client: TestClient) -> None:
    """Test case for get_pickup_list

    Get pickup list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/pickups/list",
        headers=headers,
    )

    assert response.status_code != 500
