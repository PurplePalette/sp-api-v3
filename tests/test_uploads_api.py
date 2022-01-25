# coding: utf-8

from fastapi.testclient import TestClient
from typing import Dict

from src.models.post_upload_response import PostUploadResponse  # noqa: F401


def test_upload_file(client: TestClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    data = {"file": "/path/to/file", "type": "type_example"}
    response = client.request(
        "POST",
        "/upload",
        headers=headers,
        data=data,
    )

    assert response.status_code != 500
