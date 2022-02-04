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
from src.cruds.skin import create_skin as crud_create
from src.cruds.skin import delete_skin as crud_delete
from src.cruds.skin import edit_skin as crud_edit
from src.cruds.skin import get_skin as crud_get
from src.cruds.skin import list_skin as crud_list
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchOrder, SearchQueries, SearchSort, SearchStatus
from src.models.skin import Skin

router = APIRouter()


@router.post(
    "/skins",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_skins"],
    summary="Add a skin",
)
async def add_skin(
    skin: Skin = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたスキン情報をサーバーに登録します"""
    return await crud_create(db, skin, user)


@router.delete(
    "/skins/{skinName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_skins"],
    summary="Delete a skin",
)
async def delete_skin(
    skinName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたスキンを削除します"""
    await crud_delete(db, skinName, user)
    return None


@router.patch(
    "/skins/{skinName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_skins"],
    summary="Edit a skin",
)
async def edit_skin(
    skinName: str = dependsPath,
    skin: Skin = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定したskinを編集します"""
    return await crud_edit(db, skinName, skin, user)


@router.get(
    "/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["default_skins"],
    summary="Get skin list",
)
async def get_skin_list(
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: SearchSort = dependsSort,
    order: SearchOrder = dependsOrder,
    status: SearchStatus = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetSkinListResponse:
    """It returns list of skin infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud_list(db, page, queries)


@router.get(
    "/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_skins"],
    summary="Get a skin",
)
async def get_skin(
    db: AsyncSession = dependsDatabase,
    skinName: str = dependsPath,
    localization: str = dependsLocalization,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    return await crud_get(db, skinName, localization)
