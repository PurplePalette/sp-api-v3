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
        "date": "date",
        "subtitle": "subtitle",
        "resources": {"level": "level", "icon": "icon", "bgm": "bgm"},
        "title": "title",
        "body": "body",
        "announce_name": "announceName",
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
        "/announces/{announceName}".format(announceName="announce_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_announce(client: TestClient) -> None:
    """Test case for edit_announce

    Edit announce
    """
    announce = {
        "date": "date",
        "subtitle": "subtitle",
        "resources": {"level": "level", "icon": "icon", "bgm": "bgm"},
        "title": "title",
        "body": "body",
        "announce_name": "announceName",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/announces/{announceName}".format(announceName="announce_name_example"),
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
