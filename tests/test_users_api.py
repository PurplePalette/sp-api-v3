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
    user = {"userId": "gz6xQrm79IN4BiQag78sQqYWYlC3"}

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
        "description": "description",
        "testId": "htcckfcn",
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
