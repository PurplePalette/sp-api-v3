# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


def test_get_accounts_level(client: TestClient) -> None:
    """Test case for get_accounts_level

    Get accounts level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/{levelName}".format(
            accountKey="account_key_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_accounts_levels(client: TestClient) -> None:
    """Test case for get_accounts_levels

    Get accounts level list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/levels/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
