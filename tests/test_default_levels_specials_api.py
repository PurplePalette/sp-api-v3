# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.get_level_response import GetLevelResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_announce(client: AsyncClient) -> None:
    """Test case for get_announce

    Get an announce info
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/announce_{announceName}".format(announceName="announce_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_announce_list(client: AsyncClient) -> None:
    """Test case for get_announce_list

    Get announce infos
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/announce",
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_fresh_releases(client: AsyncClient) -> None:
    """Test case for get_fresh_releases

    Get debut levels
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/debut",
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_pickups(client: AsyncClient) -> None:
    """Test case for get_pickups

    Get pickup levels
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/levels/pickups",
        headers=headers,
    )

    assert response.status_code != 500
