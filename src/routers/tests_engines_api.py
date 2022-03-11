# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.tests.engine import TestsEngineCrud
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAuthor,
    dependsDatabase,
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
crud = TestsEngineCrud()


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetEngineListResponse:
    """譜面テスト用エンドポイント/ エンジン一覧を返す"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, testId, page, queries)


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
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    return await crud.get(db, engineName, localization)
