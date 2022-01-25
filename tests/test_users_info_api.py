# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.server_info import ServerInfo  # noqa: F401


def test_get_user_server_info(client: TestClient) -> None:
    """Test case for get_user_server_info

    Get user server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/info".format(userId="user_id_example"),
        headers=headers,
    )

    assert response.status_code != 500
