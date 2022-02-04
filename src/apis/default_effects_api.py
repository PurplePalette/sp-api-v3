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
from src.cruds.effect import create_effect as crud_create
from src.cruds.effect import delete_effect as crud_delete
from src.cruds.effect import edit_effect as crud_edit
from src.cruds.effect import get_effect as crud_get
from src.cruds.effect import list_effect as crud_list
from src.models.effect import Effect
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.search_query import SearchOrder, SearchQueries, SearchSort, SearchStatus

router = APIRouter()


@router.post(
    "/effects",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_effects"],
    summary="Add an effect",
)
async def add_effect(
    db: AsyncSession = dependsDatabase,
    effect: Effect = dependsBody,
    user: FirebaseClaims = dependsFirebase,
) -> GetEffectResponse:
    """指定されたeffectをサーバーに登録します"""
    return await crud_create(db, effect, user)


@router.delete(
    "/effects/{effectName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_effects"],
    summary="Delete an effect",
)
async def delete_effect(
    db: AsyncSession = dependsDatabase,
    effectName: str = dependsPath,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """delete specified effect"""
    await crud_delete(db, effectName, user)
    return None


@router.patch(
    "/effects/{effectName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_effects"],
    summary="Edit an effect",
)
async def edit_effect(
    db: AsyncSession = dependsDatabase,
    effectName: str = dependsPath,
    effect: Effect = dependsBody,
    user: FirebaseClaims = dependsFirebase,
) -> GetEffectResponse:
    """指定されたeffectを編集します"""
    return await crud_edit(db, effectName, effect, user)


@router.get(
    "/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["default_effects"],
    summary="Get effect list",
)
async def get_effect_list(
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: SearchSort = dependsSort,
    order: SearchOrder = dependsOrder,
    status: SearchStatus = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetEffectListResponse:
    """It returns list of effect infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud_list(db, page, queries)


@router.get(
    "/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_effects"],
    summary="Get an effect",
)
async def get_effect(
    db: AsyncSession = dependsDatabase,
    effectName: str = dependsPath,
    localization: str = dependsLocalization,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    return await crud_get(db, effectName, localization)
