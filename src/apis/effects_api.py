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
from src.models.effect import Effect
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse

router = APIRouter()


@router.post(
    "/effects",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["effects"],
    summary="Add effect",
)
async def add_effect(
    effect: Effect = defaultBody,
) -> None:
    """指定されたeffectをサーバーに登録します"""
    ...


@router.delete(
    "/effects/{effectName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["effects"],
    summary="Delete effect",
)
async def delete_effect(
    effectName: str = defaultPath,
) -> None:
    """delete specified effect"""
    ...


@router.patch(
    "/effects/{effectName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["effects"],
    summary="Edit effect",
)
async def edit_effect(
    effectName: str = defaultPath,
    effect: Effect = defaultBody,
) -> None:
    """指定されたeffectを編集します"""
    ...


@router.get(
    "/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["effects"],
    summary="Get effect",
)
async def get_effect(
    effectName: str = defaultPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["effects"],
    summary="Get effect list",
)
async def get_effect_list(
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEffectListResponse:
    """It returns list of effect infos registered in this server.
    Also it can search using query params"""
    ...
