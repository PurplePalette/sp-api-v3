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
from src.apis.depends import dependsBody, dependsDatabase, dependsFirebase, dependsPath
from src.cruds.announce import create_announce as crud_create
from src.cruds.announce import delete_announce as crud_delete
from src.cruds.announce import edit_announce as crud_edit
from src.models.announce import Announce
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse

router = APIRouter()


@router.post(
    "/announces",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        409: {"description": "Conflict"},
    },
    tags=["announces"],
    summary="Add announce",
)
async def add_announce(
    announce: Announce = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> Announce:
    """アナウンスを追加します"""
    return await crud_create(db, announce, user)


@router.delete(
    "/announces/{announceName}",
    responses={
        200: {"description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
        409: {"description": "Conflict"},
    },
    tags=["announces"],
    summary="Delete announce",
)
async def delete_announce(
    announceName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたアナウンスを削除します"""
    await crud_delete(db, announceName, user)
    return None


@router.patch(
    "/announces/{announceName}",
    responses={
        200: {"description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
        409: {"description": "Conflict"},
    },
    tags=["announces"],
    summary="Edit announce",
)
async def edit_announce(
    announceName: str = dependsPath,
    announce: Announce = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定したアナウンスを編集します"""
    await crud_edit(db, announceName, announce, user)
    return None


@router.get(
    "/announces/{announceName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["announces"],
    summary="Get announce",
)
async def get_default_announce(
    announceName: str = dependsPath,
) -> GetLevelResponse:
    """指定されたアナウンスデータを返す"""
    ...


@router.get(
    "/announces/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["announces"],
    summary="Get announce list",
)
async def get_default_announces() -> GetLevelListResponse:
    """アナウンス中のデータ一覧を返す"""
    ...
