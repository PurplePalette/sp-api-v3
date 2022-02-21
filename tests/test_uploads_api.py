# coding: utf-8

import pytest
from httpx import AsyncClient
from src.models.post_upload_response import PostUploadResponse  # noqa: F401
from tests.conftest import TEST_FILE_ENDPOINT


async def require_image() -> bytes:
    async with AsyncClient() as content_client:
        data = await content_client.get(TEST_FILE_ENDPOINT + "/LevelCover/image1.png")
    return data.content


@pytest.mark.asyncio
async def test_upload_success_valid_data(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    req = {"type": "LevelCover"}
    data = await require_image()
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("image1.png", data, "image/png")},
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_upload_failed_invalid_type(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    req = {"type": "Level"}
    data = await require_image()
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("image1.png", data, "image/png")},
    )
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_upload_failed_wrong_type(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    req = {"type": "LevelBgm"}
    data = await require_image()
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("image1.png", data, "image/png")},
    )
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_upload_failed_wrong_srl(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }

    req = {"type": "LevelBgm"}
    data = await require_image()
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("image1.png", data, "image/png")},
    )
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_upload_failed_wrong_mime(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }

    req = {"type": "LevelCover"}
    data = await require_image()
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("image1.png", data, "image/webp")},
    )
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_upload_failed_bigger_than_limit(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }

    req = {"type": "LevelCover"}
    data = "".join(["a" for _ in range(1024 * 1024 * 51)]).encode("utf8")
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("dummy.png", data, "image/png")},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_upload_failed_bigger_than_define(client: AsyncClient) -> None:
    """Test case for upload_file

    Upload a file
    """

    headers = {
        "Authorization": "Bearer special-key",
    }

    req = {"type": "LevelCover"}
    data = "".join(["a" for _ in range(1024 * 1024 * 20)]).encode("utf8")
    response = await client.request(
        "POST",
        "/upload",
        headers=headers,
        data=req,
        files={"file": ("dummy.png", data, "image/png")},
    )
    assert response.status_code == 400
