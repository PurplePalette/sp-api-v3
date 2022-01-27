# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401


def test_get_users_skin(client: TestClient) -> None:
    """Test case for get_users_skin

    Get users skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/skins/{skinName}".format(
            userId="userId_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_users_skins(client: TestClient) -> None:
    """Test case for get_users_skins

    Get users skin list
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
    response = client.request(
        "GET",
        "/users/{userId}/skins/list".format(userId="userId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
