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
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import (
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
from src.cruds.background import create_background as crud_create
from src.cruds.background import delete_background as crud_delete  # noqa: F401
from src.cruds.background import edit_background as crud_edit  # noqa: F401
from src.cruds.background import get_background as crud_get  # noqa: F401
from src.cruds.background import list_background as crud_list  # noqa: F401
from src.models.background import Background
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchOrder, SearchQueries, SearchSort, SearchStatus

router = APIRouter()


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
    background: Background = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetBackgroundResponse:
    """指定された背景情報をサーバーに登録します"""
    return await crud_create(db, background, user)


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
    await crud_delete(db, backgroundName, user)
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
    background: Background = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetBackgroundResponse:
    """指定された背景情報を編集します"""
    return await crud_edit(db, backgroundName, background, user)


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
    sort: SearchSort = dependsSort,
    order: SearchOrder = dependsOrder,
    status: SearchStatus = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetBackgroundListResponse:
    """It returns list of background infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(
        keywords, author, sort, order, status, random, None, None, None, None, None
    )
    return await crud_list(db, page, queries)


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
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    return await crud_get(db, backgroundName)