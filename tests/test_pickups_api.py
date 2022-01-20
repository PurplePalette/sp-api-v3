# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_response import GetLevelResponse  # noqa: F401
from src.models.pickup import Pickup  # noqa: F401


def test_add_pickup(client: TestClient) -> None:
    """Test case for add_pickup

    Add Pickup
    """
    pickup = {"level_name": "levelName", "order": 17207}

    headers: Dict[str, str] = {}
    response = client.request(
        "POST",
        "/pickups",
        headers=headers,
        json=pickup,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_delete_pickup(client: TestClient) -> None:
    """Test case for delete_pickup

    Delete pickup
    """
    pickup = {"level_name": "levelName", "order": 17207}

    headers: Dict[str, str] = {}
    response = client.request(
        "DELETE",
        "/pickups/{pickupName}".format(pickupName="pickup_name_example"),
        headers=headers,
        json=pickup,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_fresh_levels(client: TestClient) -> None:
    """Test case for get_account_fresh_levels

    Get pickups
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/fresh-release".format(
            accountKey="account_key_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500


def test_get_account_pickup_levels(client: TestClient) -> None:
    """Test case for get_account_pickup_levels

    Get pickups
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/pickups".format(
            accountKey="account_key_example"
        ),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
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

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500
