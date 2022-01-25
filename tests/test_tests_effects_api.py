# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.get_effect_list_response import GetEffectListResponse  # noqa: F401
from src.models.get_effect_response import GetEffectResponse  # noqa: F401


def test_get_effect_test(client: TestClient) -> None:
    """Test case for get_effect_test

    Get tests effect list
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/effects/{effectName}".format(
            testId="test_id_example", effectName="effect_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_effects(client: TestClient) -> None:
    """Test case for get_tests_effects

    Get tests effects list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/effects/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
