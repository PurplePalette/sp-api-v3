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
from src.cruds.particle import create_particle as crud_create
from src.cruds.particle import delete_particle as crud_delete
from src.cruds.particle import edit_particle as crud_edit
from src.cruds.particle import get_particle as crud_get
from src.cruds.particle import list_particle as crud_list
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.particle import Particle
from src.models.search_query import SearchQueries

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
    return await crud_create(db, particle, user)


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
    await crud_delete(db, particleName, user)
    return None


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
    return await crud_edit(db, particleName, particle, user)


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
    db: AsyncSession = dependsDatabase,
) -> GetParticleListResponse:
    """It returns list of particle infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud_list(db, page, queries)


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
    localization: str = dependsLocalization,
    db: AsyncSession = dependsDatabase,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    return await crud_get(db, particleName, localization)
