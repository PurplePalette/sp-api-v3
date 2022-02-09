# coding: utf-8

import pytest
from httpx import AsyncClient
from src.models.post_upload_response import PostUploadResponse  # noqa: F401


@pytest.mark.asyncio
async def test_upload_file(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    data = {"file": "/path/to/file", "type": "type_example"}
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=data,
    )

    assert response.status_code != 500
