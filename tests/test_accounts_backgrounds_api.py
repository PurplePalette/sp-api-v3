# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


def test_get_accounts_background(client: TestClient) -> None:
    """Test case for get_accounts_background

    Get accounts background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/backgrounds/{backgroundName}".format(
            accountKey="account_key_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_accounts_backgrounds(client: TestClient) -> None:
    """Test case for get_accounts_backgrounds

    Get accounts background list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/backgrounds/list".format(
            accountKey="account_key_example"
        ),
        headers=headers,
        params=params,
    )

    assert response.status_code == 200
