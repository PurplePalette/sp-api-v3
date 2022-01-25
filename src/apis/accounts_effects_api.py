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
from src.apis.depends import (
    dependsKeywords,
    dependsLocalization,
    dependsPage,
    dependsPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_effects"],
    summary="Get accounts effect",
)
async def get_accounts_effect(
    accountKey: str = dependsPath,
    effectName: str = dependsPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["accounts_effects"],
    summary="Get accounts effect list",
)
async def get_accounts_effects(
    accountKey: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
) -> GetEffectListResponse:
    """ユーザー個別用エンドポイント/ エフェクト一覧を返す"""
    ...
