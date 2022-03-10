# coding: utf-8
from fastapi import APIRouter
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.extras.announce import AnnounceCrud
from src.models.add_announce_request import AddAnnounceRequest
from src.models.edit_announce_request import EditAnnounceRequest
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.routers.depends import (
    dependsBody,
    dependsDatabase,
    dependsFirebase,
    dependsPath,
)

router = APIRouter()
crud = AnnounceCrud()


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
    announce: AddAnnounceRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetLevelResponse:
    """アナウンスを追加します"""
    return await crud.add(db, announce, user)


@router.delete(
    "/announces/{announceName}",
    responses={
        200: {"description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
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
    await crud.delete(db, announceName, user)
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
    announce: EditAnnounceRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetLevelResponse:
    """指定したアナウンスを編集します"""
    return await crud.edit(db, announceName, announce, user)


@router.get(
    "/announces/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["announces"],
    summary="Get announce list",
)
async def get_announces(
    db: AsyncSession = dependsDatabase,
) -> GetLevelListResponse:
    """アナウンス中のデータ一覧を返す"""
    return await crud.list(db)


@router.get(
    "/announces/{announceName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["announces"],
    summary="Get announce",
)
async def get_announce(
    announceName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
) -> GetLevelResponse:
    """指定されたアナウンスデータを返す"""
    return await crud.get(db, announceName)
