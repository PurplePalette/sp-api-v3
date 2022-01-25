# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.pickup import Pickup  # noqa: F401


def test_add_pickup(client: TestClient) -> None:
    """Test case for add_pickup

    Add pickup
    """
    pickup = {"level_name": "levelName", "order": 17207}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/pickups",
        headers=headers,
        json=pickup,
    )

    assert response.status_code != 500


def test_delete_pickup(client: TestClient) -> None:
    """Test case for delete_pickup

    Delete pickup
    """
    pickup = {"level_name": "levelName", "order": 17207}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/pickups/{pickupName}".format(pickupName="pickup_name_example"),
        headers=headers,
        json=pickup,
    )

    assert response.status_code != 500


def test_get_pickup(client: TestClient) -> None:
    """Test case for get_pickup

    Get pickup
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/pickups/{pickupName}".format(pickupName="pickup_name_example"),
        headers=headers,
    )

    assert response.status_code != 500
