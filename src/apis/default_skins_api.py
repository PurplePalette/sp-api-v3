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
    status,
)
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import (
    dependsBody,
    dependsDatabase,
    dependsFirebase,
    dependsKeywords,
    dependsLocalization,
    dependsPage,
    dependsPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
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
    ...


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
    ...


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
    ...


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
    skinName: str = dependsPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


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
) -> GetSkinListResponse:
    """It returns list of skin infos registered in this server.
    Also it can search using query params"""
    ...
