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
    with open("./tests/toy_figure_girl.png", "rb") as f:
        data = f.read()
    req = {"type": "LevelCover"}
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("toy_figure_girl.png", data, "image/png")},
    )
    assert response.status_code == 200
