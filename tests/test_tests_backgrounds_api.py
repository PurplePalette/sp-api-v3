# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_background_list_response import (
    GetBackgroundListResponse,
)  # noqa: F401
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


def test_get_background_test(client: TestClient) -> None:
    """Test case for get_background_test

    Get tests background
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/backgrounds/{backgroundName}".format(
            testId="test_id_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_backgrounds(client: TestClient) -> None:
    """Test case for get_tests_backgrounds

    Get tests background list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/backgrounds/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
