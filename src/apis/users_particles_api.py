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
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse

router = APIRouter()


@router.get(
    "/users/{userId}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_particles"],
    summary="Get users particle",
)
async def get_users_particle(
    userId: str = dependsPath,
    particleName: str = dependsPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_particles"],
    summary="Get users particle list",
)
async def get_users_particles(
    userId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetParticleListResponse:
    """ユーザー個別用エンドポイント/ パーティクル一覧を返す"""
    ...
