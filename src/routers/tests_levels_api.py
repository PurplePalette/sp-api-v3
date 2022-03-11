# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.tests.level import TestsLevelCrud
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAuthor,
    dependsDatabase,
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

router = APIRouter()
crud = TestsLevelCrud()


@router.get(
    "/tests/{testId}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_levels"],
    summary="Get tests level list",
)
async def get_tests_levels(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    rating_min: int = dependsRatingMin,
    rating_max: int = dependsRatingMax,
    genre: int = dependsGenre,
    length: int = dependsLength,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetLevelListResponse:
    """譜面テスト用エンドポイント/ 譜面一覧を返す"""
    queries = SearchQueries(
        localization,
        keywords,
        author,
        sort,
        order,
        status,
        random,
        rating_min,
        rating_max,
        genre,
        length,
    )
    return await crud.list(db, testId, page, queries)


@router.get(
    "/tests/{testId}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_levels"],
    summary="Get tests level",
)
async def get_level_test(
    testId: str = dependsPath,
    levelName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    return await crud.get(db, levelName, localization)
