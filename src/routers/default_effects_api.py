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
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.defaults.effect import EffectCrud
from src.models.add_effect_request import AddEffectRequest
from src.models.effect import Effect
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAddEffect,
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
from src.security_api import FirebaseClaims

router = APIRouter()
crud = EffectCrud()


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
    add_effect_request: AddEffectRequest = dependsAddEffect,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetEffectResponse:
    """指定されたeffectをサーバーに登録します"""
    return await crud.add(db, add_effect_request, user)


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
    await crud.delete(db, effectName, user)
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
    return await crud.edit(db, effectName, effect, user)


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetEffectListResponse:
    """It returns list of effect infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, page, queries)


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
    return await crud.get(db, effectName, localization)
