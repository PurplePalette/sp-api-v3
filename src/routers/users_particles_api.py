# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.users.particle import UsersParticleCrud
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.search_query import SearchQueries
from src.routers.depends import (
    dependsAuthor,
    dependsDatabase,
    dependsKeywords,
    dependsLocalization,
    dependsOrder,
    dependsPage,
    dependsPath,
    dependsRandom,
    dependsSort,
    dependsStatus,
)

router = APIRouter()
crud = UsersParticleCrud()


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
    db: AsyncSession = dependsDatabase,
) -> GetParticleListResponse:
    """譜面テスト用エンドポイント/ パーティクル一覧を返す"""
    queries = SearchQueries(localization, keywords, author, sort, order, status, random)
    return await crud.list(db, userId, page, queries)


@router.get(
    "/users/{userId}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_particles"],
    summary="Get users particle",
)
async def get_particle_user(
    userId: str = dependsPath,
    particleName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    localization: str = dependsLocalization,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    return await crud.get(db, particleName, localization)
