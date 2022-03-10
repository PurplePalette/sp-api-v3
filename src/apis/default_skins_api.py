# coding: utf-8

from fastapi import APIRouter
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
from src.cruds.defaults.skin import SkinCrud
from src.models.add_skin_request import AddSkinRequest
from src.models.edit_skin_request import EditSkinRequest
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchQueries

router = APIRouter()
crud = SkinCrud()


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
    skin: AddSkinRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetSkinResponse:
    """指定されたスキン情報をサーバーに登録します"""
    return await crud.add(db, skin, user)


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
    await crud.delete(db, skinName, user)
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
    skin: EditSkinRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetSkinResponse:
    """指定したskinを編集します"""
    return await crud.edit(db, skinName, skin, user)


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetSkinListResponse:
    """It returns list of skin infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, page, queries)


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
    return await crud.get(db, skinName, localization)
