# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_level_list_response import GetLevelListResponse  # noqa: F401
from src.models.get_level_response import GetLevelResponse  # noqa: F401


def test_get_level_test(client: TestClient) -> None:
    """Test case for get_level_test

    Get tests level
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/levels/{levelName}".format(
            testId="test_id_example", levelName="level_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_levels(client: TestClient) -> None:
    """Test case for get_tests_levels

    Get tests level list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/levels/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
