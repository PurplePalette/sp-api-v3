# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.tests.background import TestsBackgroundCrud
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
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
crud = TestsBackgroundCrud()


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetBackgroundListResponse:
    """背景一覧を返す"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, testId, page, queries)


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
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    return await crud.get(db, backgroundName, localization)
