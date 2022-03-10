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
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.routers.depends import (
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

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_skins"],
    summary="Get accounts skin",
)
async def get_accounts_skin(
    accountKey: str = dependsPath,
    skinName: str = dependsPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_skins"],
    summary="Get accounts skin list",
)
async def get_accounts_skins(
    accountKey: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetSkinListResponse:
    """ユーザー個別用エンドポイント/ スキン一覧を返す"""
    ...
