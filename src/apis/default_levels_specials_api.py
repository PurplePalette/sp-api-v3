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
)
from src.apis.depends import dependsPath
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_response import GetLevelResponse

router = APIRouter()


@router.get(
    "/levels/announce_{announceName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_levels_specials"],
    summary="Get an announce info",
)
async def get_announce(
    announceName: str = dependsPath,
) -> GetLevelResponse:
    """指定されたアナウンス情報を表示します"""
    ...


@router.get(
    "/levels/announce",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_levels_specials"],
    summary="Get announce infos",
)
async def get_announce_list() -> GetLevelResponse:
    """現在のアナウンス一覧を取得します"""
    ...


@router.get(
    "/levels/debut",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["default_levels_specials"],
    summary="Get debut levels",
)
async def get_fresh_releases() -> GetLevelResponse:
    """新規譜面作者の譜面のみを返すエンドポイント"""
    ...


@router.get(
    "/levels/pickups",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["default_levels_specials"],
    summary="Get pickup levels",
)
async def get_pickups() -> GetLevelResponse:
    """管理者の指定したおすすめ譜面などを返すエンドポイント"""
    ...
