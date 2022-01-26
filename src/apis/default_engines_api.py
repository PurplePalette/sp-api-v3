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
    dependsSort,
    dependsOrder,
    dependsStatus,
    dependsAuthor,
    dependsRandom,
)
from src.models.engine import Engine
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse

router = APIRouter()


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
    engine: Engine = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたゲームエンジンをサーバーに登録します"""
    ...


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
    ...


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
    engine: Engine = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたengineを編集します"""
    ...


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
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


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
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetEngineListResponse:
    """It returns list of engine infos registered in this server.
    Also it can search using query params"""
    ...
