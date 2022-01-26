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
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse

router = APIRouter()


@router.get(
    "/tests/{testId}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_skins"],
    summary="Get tests skin",
)
async def get_skin_test(
    testId: str = dependsPath,
    skinName: str = dependsPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_skins"],
    summary="Get tests skin list",
)
async def get_tests_skins(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetSkinListResponse:
    """譜面テスト用エンドポイント/ スキン一覧を返す(一般のスキンリストと同じのが返される)"""
    ...
