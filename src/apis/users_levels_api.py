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
from src.apis.depends import (
    dependsAuthor,
    dependsGenre,
    dependsKeywords,
    dependsLength,
    dependsLocalization,
    dependsOrder,
    dependsPage,
    dependsPath,
    dependsRandom,
    dependsRatingMax,
    dependsRatingMin,
    dependsSort,
    dependsStatus,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse

router = APIRouter()


@router.get(
    "/users/{userId}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_levels"],
    summary="Get users level",
)
async def get_users_level(
    userId: str = dependsPath,
    levelName: str = dependsPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_levels"],
    summary="Get users level list",
)
async def get_users_levels(
    userId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    rating_min: int = dependsRatingMin,
    rating_max: int = dependsRatingMax,
    genre: str = dependsGenre,
    length: str = dependsLength,
    random: int = dependsRandom,
) -> GetLevelListResponse:
    """ユーザー個別用エンドポイント/ 背景一覧を返す"""
    ...
