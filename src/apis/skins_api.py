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
from src.apis.defaults import (
    defaultBody,
    defaultKeywords,
    defaultLocalization,
    defaultPage,
    defaultPath,
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
    tags=["skins"],
    summary="Add skin",
)
async def add_skin(
    skin: Skin = defaultBody,
) -> None:
    """指定されたスキン情報をサーバーに登録します"""
    ...


@router.delete(
    "/skins/{skinName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["skins"],
    summary="Delete skin",
)
async def delete_skin(
    skinName: str = defaultPath,
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
    tags=["skins"],
    summary="Edit skin",
)
async def edit_skin(
    skinName: str = defaultPath,
    skin: Skin = defaultBody,
) -> None:
    """指定したskinを編集します"""
    ...


@router.get(
    "/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["skins"],
    summary="Get skin",
)
async def get_skin(
    skinName: str = defaultPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["skins"],
    summary="Get skin list",
)
async def get_skin_list(
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetSkinListResponse:
    """It returns list of skin infos registered in this server.
    Also it can search using query params"""
    ...
