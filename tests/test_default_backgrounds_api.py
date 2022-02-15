# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.background import Background  # noqa: F401
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


@pytest.mark.asyncio
async def test_add_background_success_valid_data(client: AsyncClient) -> None:
    """Test case for add_background

    Add a background success with valid data
    """
    add_background_request = {
        "image": "image",
        "thumbnail": "thumbnail",
        "data": "data",
        "configuration": "configuration",
        "author": "author",
        "subtitle": "subtitle",
        "description": "No description",
        "title": "newTitle",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "POST",
        "/backgrounds",
        headers=headers,
        json=add_background_request,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_background_failed_invalid_data(client: AsyncClient) -> None:
    """Test case for add_background

    Add a background failed with invalid data
    """
    add_background_request = {
        "author": "author",
        "subtitle": "subtitle",
        "description": "No description",
        "title": "newTitle",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "POST",
        "/backgrounds",
        headers=headers,
        json=add_background_request,
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_add_background_failed_no_auth(client: AsyncClient) -> None:
    """Test case for add_background

    Add a background failed with no auth
    """
    add_background_request = {
        "image": "image",
        "thumbnail": "thumbnail",
        "data": "data",
        "configuration": "configuration",
        "author": "author",
        "subtitle": "subtitle",
        "description": "No description",
        "title": "newTitle",
    }
    response = await client.request(
        "POST",
        "/backgrounds",
        json=add_background_request,
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_add_background_failed_invalid_auth(client: AsyncClient) -> None:
    """Test case for add_background

    Add a background failed with invalid auth
    """
    add_background_request = {
        "image": "image",
        "thumbnail": "thumbnail",
        "data": "data",
        "configuration": "configuration",
        "author": "author",
        "subtitle": "subtitle",
        "description": "No description",
        "title": "newTitle",
    }
    headers = {
        "Authorization": "Bearer invalid-key",
    }
    response = await client.request(
        "POST",
        "/backgrounds",
        headers=headers,
        json=add_background_request,
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_background_success_admin(client: AsyncClient) -> None:
    """Test case for delete_background

    Delete a background
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_background_success_owner(client: AsyncClient) -> None:
    """Test case for delete_background

    Delete a background
    """

    headers = {
        "Authorization": "Bearer normal-key",
    }
    response = await client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_background_failed_invalid_auth(client: AsyncClient) -> None:
    """Test case for delete_background

    Delete a background
    """
    headers = {
        "Authorization": "Bearer invalid-key",
    }
    response = await client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
    )

    assert response.status_code == 403


@pytest.mark.asyncio
async def test_delete_background_failed_no_auth(client: AsyncClient) -> None:
    """Test case for delete_background

    Delete a background
    """

    response = await client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_edit_background_success_valid_data(client: AsyncClient) -> None:
    """Test case for edit_background

    Edit a background
    """
    background = {
        "title": "b",
        "titleEn": "b",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
        json=background,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_background_success_ignore_data(client: AsyncClient) -> None:
    """Test case for edit_background

    Edit a background
    """
    background = {
        "name": "bbb",
        "userId": 2,
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
        json=background,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_edit_background_failed_invalid_data(client: AsyncClient) -> None:
    """Test case for edit_background

    Edit a background
    """
    background = {
        "title": "香風智乃" * 100,
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
        json=background,
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_background_success_found(client: AsyncClient) -> None:
    """Test case for get_background

    Get a background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/backgrounds/{backgroundName}".format(backgroundName="a"),
        headers=headers,
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_background_failed_not_found(client: AsyncClient) -> None:
    """Test case for get_background

    Get a background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/backgrounds/{backgroundName}".format(backgroundName="not_found"),
        headers=headers,
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_background_list(client: AsyncClient) -> None:
    """Test case for get_background_list

    Get background list
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
    response = await client.request(
        "GET",
        "/backgrounds/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
