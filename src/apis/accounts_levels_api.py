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
from src.apis.depends import (
    dependsKeywords,
    dependsLocalization,
    dependsPage,
    dependsPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels"],
    summary="Get accounts level",
)
async def get_accounts_level(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["accounts_levels"],
    summary="Get accounts level list",
)
async def get_accounts_levels(
    accountKey: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
) -> GetLevelListResponse:
    """ユーザー個別用エンドポイント/ 譜面一覧を返す"""
    ...
