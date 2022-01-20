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

from src.models.extra_models import TokenModel  # noqa: F401
from src.models.background import Background
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse


router = APIRouter()


@router.post(
    "/backgrounds",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["backgrounds"],
    summary="Add background",
)
async def add_background(
    background: Background = Body(None, description=""),
) -> None:
    """指定された背景情報をサーバーに登録します"""
    ...


@router.delete(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["backgrounds"],
    summary="Delete background",
)
async def delete_background(
    backgroundName: str = Path(None, description=""),
) -> None:
    """Delete specified background"""
    ...


@router.patch(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["backgrounds"],
    summary="Edit background",
)
async def edit_background(
    backgroundName: str = Path(None, description=""),
    background: Background = Body(None, description=""),
) -> None:
    """指定された背景情報を編集します"""
    ...


@router.get(
    "/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["backgrounds"],
    summary="Get background",
)
async def get_background(
    backgroundName: str = Path(None, description=""),
) -> GetBackgroundResponse:
    """It returns specified background info It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
    },
    tags=["backgrounds"],
    summary="Get background list",
)
async def get_background_list(
    localization: str = Query(None, description="It localizes response items if possible", min_length=1, max_length=50),
    page: int = Query(1, description="It filters items for pagination if possible", ge=0, le=10000),
    keywords: str = Query(None, description="It filters items for search from list if possible", min_length=1, max_length=300),
) -> GetBackgroundListResponse:
    """It returns list of background infos registered in this server Also it can search using query params"""
    ...
