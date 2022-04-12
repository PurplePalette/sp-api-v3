# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.pickup import Pickup  # noqa: F401


@pytest.mark.asyncio
async def test_add_pickup(client: AsyncClient) -> None:
    """Test case for add_pickup

    Add pickup
    """
    pickup = {"name": "name", "order": 17207}

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "POST",
        "/pickups",
        headers=headers,
        json=pickup,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_pickup(client: AsyncClient) -> None:
    """Test case for delete_pickup

    Delete pickup
    """

    headers = {
        "Authorization": "Bearer kafuu_chino",
    }
    response = await client.request(
        "DELETE",
        "/pickups/{pickupName}".format(pickupName="pickup_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_pickup(client: AsyncClient) -> None:
    """Test case for get_pickup

    Get pickup
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/pickups/{pickupName}".format(pickupName="pickup_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_pickup_list(client: AsyncClient) -> None:
    """Test case for get_pickup_list

    Get pickup list
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/pickups/list",
        headers=headers,
    )

    assert response.status_code != 500
