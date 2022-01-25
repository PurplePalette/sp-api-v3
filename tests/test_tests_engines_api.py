# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_engine_list_response import GetEngineListResponse  # noqa: F401
from src.models.get_engine_response import GetEngineResponse  # noqa: F401


def test_get_engine_test(client: TestClient) -> None:
    """Test case for get_engine_test

    Get tests engine
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/engines/{engineName}".format(
            testId="test_id_example", engineName="engine_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_engines(client: TestClient) -> None:
    """Test case for get_tests_engines

    Get tests engine list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/engines/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
