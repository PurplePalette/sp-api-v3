# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.users.effect import UsersEffectCrud
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
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
crud = UsersEffectCrud()


@router.get(
    "/users/{userId}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_effects"],
    summary="Get users effects list",
)
async def get_users_effects(
    userId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetEffectListResponse:
    """譜面テスト用エンドポイント/ エフェクト一覧を返す"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, userId, page, queries)


@router.get(
    "/users/{userId}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_effects"],
    summary="Get users effect list",
)
async def get_effect_user(
    userId: str = dependsPath,
    effectName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    return await crud.get(db, effectName, localization)
