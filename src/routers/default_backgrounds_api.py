# coding: utf-8
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.defaults.background import BackgroundCrud
from src.models.add_background_request import AddBackgroundRequest
from src.models.edit_background_request import EditBackgroundRequest
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAddBackground,
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
from src.security_api import FirebaseClaims

router = APIRouter()
crud = BackgroundCrud()


@router.post(
    "/backgrounds",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_backgrounds"],
    summary="Add a background",
)
async def add_background(
    add_background_request: AddBackgroundRequest = dependsAddBackground,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetBackgroundResponse:
    """指定された背景情報をサーバーに登録します"""
    return await crud.add(db, add_background_request, user)


@router.delete(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_backgrounds"],
    summary="Delete a background",
)
async def delete_background(
    backgroundName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """Delete specified background"""
    await crud.delete(db, backgroundName, user)
    return None


@router.patch(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_backgrounds"],
    summary="Edit a background",
)
async def edit_background(
    backgroundName: str = dependsPath,
    edit_background_request: EditBackgroundRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetBackgroundResponse:
    """指定された背景情報を編集します"""
    return await crud.edit(db, backgroundName, edit_background_request, user)


@router.get(
    "/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
    },
    tags=["default_backgrounds"],
    summary="Get background list",
)
async def get_background_list(
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
    """It returns list of background infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, page, queries)


@router.get(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_backgrounds"],
    summary="Get a background",
)
async def get_background(
    db: AsyncSession = dependsDatabase,
    backgroundName: str = dependsPath,
    localization: str = dependsLocalization,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    return await crud.get(db, backgroundName, localization)
