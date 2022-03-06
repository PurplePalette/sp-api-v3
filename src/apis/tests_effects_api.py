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
from src.apis.depends import (
    dependsAuthor,
    dependsKeywords,
    dependsLocalization,
    dependsOrder,
    dependsPage,
    dependsPath,
    dependsRandom,
    dependsSort,
    dependsStatus,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse

router = APIRouter()


@router.get(
    "/tests/{testId}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_effects"],
    summary="Get tests effect list",
)
async def get_effect_test(
    testId: str = dependsPath,
    effectName: str = dependsPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_effects"],
    summary="Get tests effects list",
)
async def get_tests_effects(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetEffectListResponse:
    """譜面テスト用エンドポイント/ エフェクト一覧を返す(一般のエフェクトリストと同じのが返される)"""
    ...
