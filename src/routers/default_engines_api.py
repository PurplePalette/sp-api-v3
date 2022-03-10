# coding: utf-8
from fastapi import APIRouter
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.defaults.engine import EngineCrud
from src.models.add_engine_request import AddEngineRequest
from src.models.edit_engine_request import EditEngineRequest
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAuthor,
    dependsBody,
    dependsDatabase,
    dependsFirebase,
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
crud = EngineCrud()


@router.post(
    "/engines",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_engines"],
    summary="Add an engine",
)
async def add_engine(
    engine: AddEngineRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetEngineResponse:
    """指定されたゲームエンジンをサーバーに登録します"""
    return await crud.add(db, engine, user)


@router.delete(
    "/engines/{engineName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_engines"],
    summary="Delete an engine",
)
async def delete_engine(
    engineName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """delete a engine"""
    await crud.delete(db, engineName, user)
    return None


@router.patch(
    "/engines/{engineName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_engines"],
    summary="Edit an engine",
)
async def edit_engine(
    engineName: str = dependsPath,
    engine: EditEngineRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetEngineResponse:
    """指定されたengineを編集します"""
    return await crud.edit(db, engineName, engine, user)


@router.get(
    "/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
    },
    tags=["default_engines"],
    summary="Get engine list",
)
async def get_engine_list(
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
    """It returns list of engine infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, page, queries)


@router.get(
    "/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_engines"],
    summary="Get an engine",
)
async def get_engine(
    engineName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    return await crud.get(db, engineName, localization)
