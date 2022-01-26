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
    dependsKeywords,
    dependsLocalization,
    dependsOrder,
    dependsPage,
    dependsPath,
    dependsRandom,
    dependsSort,
    dependsStatus,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse

router = APIRouter()


@router.get(
    "/users/{userId}/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_engines"],
    summary="Get users engine",
)
async def get_users_engine(
    userId: str = dependsPath,
    engineName: str = dependsPath,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_engines"],
    summary="Get users engine list",
)
async def get_users_engines(
    userId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetEngineListResponse:
    """ユーザー個別用エンドポイント/ エンジン一覧を返す"""
    ...
