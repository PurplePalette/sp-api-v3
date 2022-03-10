# coding: utf-8

from fastapi import APIRouter
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import (
    dependsAddParticle,
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
from src.cruds.defaults.particle import ParticleCrud
from src.models.add_particle_request import AddParticleRequest
from src.models.edit_particle_request import EditParticleRequest
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.search_query import SearchQueries

router = APIRouter()
crud = ParticleCrud()


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
    particle: AddParticleRequest = dependsAddParticle,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetParticleResponse:
    """指定されたパーティクル情報をサーバーに登録します"""
    return await crud.add(db, particle, user)


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
    await crud.delete(db, particleName, user)
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
    particle: EditParticleRequest = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> GetParticleResponse:
    """指定したparticleを編集します"""
    return await crud.edit(db, particleName, particle, user)


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
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
    db: AsyncSession = dependsDatabase,
) -> GetParticleListResponse:
    """It returns list of particle infos registered in this server.
    Also it can search using query params"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, page, queries)


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
    return await crud.get(db, particleName, localization)
