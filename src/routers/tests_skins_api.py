# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.tests.skin import TestsSkinCrud
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
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
crud = TestsSkinCrud()


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetSkinListResponse:
    """譜面テスト用エンドポイント/ スキン一覧を返す"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, testId, page, queries)


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
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    return await crud.get(db, skinName, localization)
