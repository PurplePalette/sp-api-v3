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
    dependsSort,
    dependsOrder,
    dependsStatus,
    dependsAuthor,
    dependsRandom,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse

router = APIRouter()


@router.get(
    "/tests/{testId}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests_particles"],
    summary="Get tests particle",
)
async def get_particle_test(
    testId: str = dependsPath,
    particleName: str = dependsPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["tests_particles"],
    summary="Get tests particle list",
)
async def get_tests_particles(
    testId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetParticleListResponse:
    """譜面テスト用エンドポイント/ パーティクル一覧を返す(一般の背景リストと同じのが返される)"""
    ...
