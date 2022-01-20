# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from src.models.extra_models import TokenModel  # noqa: F401
from src.models.announce import Announce
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse


router = APIRouter()


@router.post(
    "/announces",
    responses={
        200: {"description": "OK"},
    },
    tags=["announces"],
    summary="Add announce",
)
async def add_announce(
    announce: Announce = Body(None, description=""),
) -> None:
    """譜面のピックアップを追加します"""
    ...


@router.delete(
    "/announces/{announceName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["announces"],
    summary="Delete announce",
)
async def delete_announce(
    announceName: str = Path(None, description=""),
) -> None:
    """指定されたアナウンスを削除します"""
    ...


@router.patch(
    "/announces/{announceName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["announces"],
    summary="Edit announce",
)
async def edit_announce(
    announceName: str = Path(None, description=""),
    announce: Announce = Body(None, description=""),
) -> None:
    """指定したアナウンスを編集します"""
    ...


@router.get(
    "/announces/{announceName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["announces"],
    summary="Get announce",
)
async def get_announce(
    announceName: str = Path(None, description=""),
) -> GetLevelResponse:
    """指定されたアナウンスデータを返す"""
    ...


@router.get(
    "/announces/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["announces"],
    summary="Get announce list",
)
async def get_announces(
) -> GetLevelListResponse:
    """アナウンス中のデータ一覧を返す"""
    ...


@router.get(
    "/pickups/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["announces"],
    summary="Get pickup list",
)
async def get_pickup_list(
) -> GetLevelListResponse:
    """ピックアップ中のデータ一覧を返す"""
    ...
