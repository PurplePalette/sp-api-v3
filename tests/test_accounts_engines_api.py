# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


def test_get_accounts_engine(client: TestClient) -> None:
    """Test case for get_accounts_engine

    Get accounts engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/accounts/{accountKey}/engines/{engineName}".format(
            accountKey="account_key_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_accounts_engines(client: TestClient) -> None:
    """Test case for get_accounts_engines

    Get accounts engine list
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
        "/accounts/{accountKey}/engines/list".format(accountKey="account_key_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
