# coding: utf-8

from fastapi import APIRouter
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.defaults.level import LevelCrud
from src.models.add_level_request import AddLevelRequest
from src.models.edit_level_request import EditLevelRequest
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAuthor,
    dependsBody,
    dependsDatabase,
    dependsFirebase,
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
crud = LevelCrud()


@router.post(
    "/levels",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_levels"],
    summary="Add a level",
)
async def add_level(
    level: AddLevelRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetLevelResponse:
    """指定された譜面情報をサーバーに登録します"""
    return await crud.add(db, level, user)


@router.delete(
    "/levels/{levelName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_levels"],
    summary="Delete a level",
)
async def delete_level(
    levelName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたレベルを削除します"""
    await crud.delete(db, levelName, user)
    return None


@router.patch(
    "/levels/{levelName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_levels"],
    summary="Edit a level",
)
async def edit_level(
    levelName: str = dependsPath,
    level: EditLevelRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetLevelResponse:
    """指定されたlevelを編集します"""
    return await crud.edit(db, levelName, level, user)


@router.get(
    "/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["default_levels"],
    summary="Get level list",
)
async def get_level_list(
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
    """It returns list of level infos registered in this server.
    Also it can search using query params"""
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
    return await crud.list(db, page, queries)


@router.get(
    "/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_levels"],
    summary="Get a level",
)
async def get_level(
    localization: str = dependsLocalization,
    levelName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    return await crud.get(db, levelName, localization)
