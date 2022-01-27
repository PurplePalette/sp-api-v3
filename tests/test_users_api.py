# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_user_list_response import GetUserListResponse  # noqa: F401
from src.models.user import User  # noqa: F401


def test_add_user(client: TestClient) -> None:
    """Test case for add_user

    Add a user
    """
    user = {
        "updatedTime": 0,
        "total": {
            "favorites": 0,
            "plays": 0,
            "publish": {
                "skins": 9,
                "effects": 5,
                "engines": 5,
                "backgrounds": 1,
                "particles": 2,
                "levels": 7,
            },
            "likes": 0,
        },
        "is_deleted": 0,
        "description": "description",
        "createdTime": 0,
        "testId": "htcckfcn",
        "is_admin": 0,
        "userId": "gz6xQrm79IN4BiQag78sQqYWYlC3",
        "account_key": "super_secret_key",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/users",
        headers=headers,
        json=user,
    )

    assert response.status_code != 500


def test_delete_user(client: TestClient) -> None:
    """Test case for delete_user

    Delete a user
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/users/{userId}".format(userId="userId_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_user(client: TestClient) -> None:
    """Test case for edit_user

    Edit a user
    """
    user = {
        "updatedTime": 0,
        "total": {
            "favorites": 0,
            "plays": 0,
            "publish": {
                "skins": 9,
                "effects": 5,
                "engines": 5,
                "backgrounds": 1,
                "particles": 2,
                "levels": 7,
            },
            "likes": 0,
        },
        "is_deleted": 0,
        "description": "description",
        "createdTime": 0,
        "testId": "htcckfcn",
        "is_admin": 0,
        "userId": "gz6xQrm79IN4BiQag78sQqYWYlC3",
        "account_key": "super_secret_key",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/users/{userId}".format(userId="userId_example"),
        headers=headers,
        json=user,
    )

    assert response.status_code != 500


def test_get_user(client: TestClient) -> None:
    """Test case for get_user

    Get a user
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}".format(userId="userId_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_user_list(client: TestClient) -> None:
    """Test case for get_user_list

    Get user list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/list",
        headers=headers,
    )

    assert response.status_code != 500
