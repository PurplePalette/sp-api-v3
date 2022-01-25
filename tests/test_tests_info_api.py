# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.server_info import ServerInfo  # noqa: F401


def test_get_test_server_info(client: TestClient) -> None:
    """Test case for get_test_server_info

    Get test server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/info".format(testId="test_id_example"),
        headers=headers,
    )

    assert response.status_code != 500
