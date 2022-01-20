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
from src.apis.defaults import (
    defaultBody,
    defaultKeywords,
    defaultLocalization,
    defaultPage,
    defaultPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.level import Level

router = APIRouter()


@router.post(
    "/levels",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["levels"],
    summary="Add level",
)
async def add_level(
    level: Level = defaultBody,
) -> None:
    """指定された譜面情報をサーバーに登録します"""
    ...


@router.delete(
    "/levels/{levelName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["levels"],
    summary="Delete a level",
)
async def delete_level(
    levelName: str = defaultPath,
) -> None:
    """指定されたレベルを削除します"""
    ...


@router.patch(
    "/levels/{levelName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["levels"],
    summary="Edit level",
)
async def edit_level(
    levelName: str = defaultPath,
    level: Level = defaultBody,
) -> None:
    """指定されたlevelを編集します"""
    ...


@router.get(
    "/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["levels"],
    summary="Get level",
)
async def get_level(
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["levels"],
    summary="Get level list",
)
async def get_level_list(
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetLevelListResponse:
    """It returns list of level infos registered in this server.
    Also it can search using query params"""
    ...
