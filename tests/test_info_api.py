# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.server_info import ServerInfo  # noqa: F401


def test_get_server_info(client: TestClient) -> None:
    """Test case for get_server_info

    Get server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/info",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
