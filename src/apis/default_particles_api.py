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
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.particle import Particle

router = APIRouter()


@router.post(
    "/particles",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["default_particles"],
    summary="Add a particle",
)
async def add_particle(
    particle: Particle = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたパーティクル情報をサーバーに登録します"""
    ...


@router.delete(
    "/particles/{particleName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["default_particles"],
    summary="Delete a particle",
)
async def delete_particle(
    particleName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定されたパーティクルを削除する"""
    ...


@router.patch(
    "/particles/{particleName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["default_particles"],
    summary="Edit a particle",
)
async def edit_particle(
    particleName: str = dependsPath,
    particle: Particle = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定したparticleを編集します"""
    ...


@router.get(
    "/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default_particles"],
    summary="Get a particle",
)
async def get_particle(
    particleName: str = dependsPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["default_particles"],
    summary="Get particle list",
)
async def get_particle_list(
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: str = dependsSort,
    order: str = dependsOrder,
    status: str = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetParticleListResponse:
    """It returns list of particle infos registered in this server.
    Also it can search using query params"""
    ...
