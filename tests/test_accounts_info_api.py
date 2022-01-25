# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.server_info import ServerInfo  # noqa: F401


def test_get_accounts_server_info(client: TestClient) -> None:
    """Test case for get_accounts_server_info

    Get account server info
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/info".format(accountKey="account_key_example"),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code != 500
