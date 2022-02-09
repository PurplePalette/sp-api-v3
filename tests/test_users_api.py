# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_user_list_response import GetUserListResponse  # noqa: F401
from src.models.user import User  # noqa: F401


@pytest.mark.asyncio
async def test_add_user(client: AsyncClient) -> None:
    """Test case for add_user

    Add a user
    """
    user = {
        "userId": "gz6xQrm79IN4BiQag78sQqYWYlC3",
        "accountId": "starKey",
        "testId": "password",
        "description": "description",
        "isDeleted": 0,
        "isAdmin": 0,
    }

    headers = {
        "Authorization": "Bearer StarApi",
    }
    response = await client.request(
        "POST",
        "/users",
        headers=headers,
        json=user,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient) -> None:
    """Test case for delete_user

    Delete a user
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/users/{userId}".format(userId="userId_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_user(client: AsyncClient) -> None:
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
    response = await client.request(
        "PATCH",
        "/users/{userId}".format(userId="userId_example"),
        headers=headers,
        json=user,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_user(client: AsyncClient) -> None:
    """Test case for get_user

    Get a user
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}".format(userId="special-key"),
        headers=headers,
    )
    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_user_with_auth(client: AsyncClient) -> None:
    """Test case for get_user

    Get a user using auth
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "GET",
        "/users/{userId}".format(userId="special-key"),
        headers=headers,
    )
    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_user_list(client: AsyncClient) -> None:
    """Test case for get_user_list

    Get user list
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/list",
        headers=headers,
    )

    assert response.status_code != 500
