# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_background_list_response import (
    GetBackgroundListResponse,
)  # noqa: F401
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


def test_get_users_background(client: TestClient) -> None:
    """Test case for get_users_background

    Get users background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/backgrounds/{backgroundName}".format(
            userId="user_id_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_users_backgrounds(client: TestClient) -> None:
    """Test case for get_users_backgrounds

    Get users background list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/backgrounds/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
