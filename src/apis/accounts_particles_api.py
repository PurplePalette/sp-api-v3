# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import APIRouter  # noqa: F401
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
    "/accounts/{accountKey}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_particles"],
    summary="Get accounts particle",
)
async def get_accounts_particle(
    accountKey: str = dependsPath,
    particleName: str = dependsPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_particles"],
    summary="Get accounts particle list",
)
async def get_accounts_particles(
    accountKey: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetParticleListResponse:
    """ユーザー個別用エンドポイント/ パーティクル一覧を返す"""
    ...
