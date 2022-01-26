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
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse

router = APIRouter()


@router.get(
    "/tests/{testId}/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_backgrounds"],
    summary="Get tests background",
)
async def get_background_test(
    testId: str = dependsPath,
    backgroundName: str = dependsPath,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_backgrounds"],
    summary="Get tests background list",
)
async def get_tests_backgrounds(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetBackgroundListResponse:
    """譜面テスト用エンドポイント/ 背景一覧を返す(一般の背景リストと同じのが返される)"""
    ...
