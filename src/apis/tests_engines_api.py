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
    "/tests/{testId}/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_engines"],
    summary="Get tests engine",
)
async def get_engine_test(
    testId: str = dependsPath,
    engineName: str = dependsPath,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_engines"],
    summary="Get tests engine list",
)
async def get_tests_engines(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetEngineListResponse:
    """譜面テスト用エンドポイント/ エンジン一覧を返す(一般のエンジンリストと同じのが返される)"""
    ...
