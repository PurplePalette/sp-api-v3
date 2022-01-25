# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


def test_get_users_engine(client: TestClient) -> None:
    """Test case for get_users_engine

    Get users engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/engines/{engineName}".format(
            userId="user_id_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_users_engines(client: TestClient) -> None:
    """Test case for get_users_engines

    Get users engine list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/users/{userId}/engines/list".format(userId="user_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
