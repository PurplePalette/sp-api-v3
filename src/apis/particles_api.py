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
    tags=["particles"],
    summary="Add particle",
)
async def add_particle(
    particle: Particle = defaultBody,
) -> None:
    """指定されたパーティクル情報をサーバーに登録します"""
    ...


@router.delete(
    "/particles/{particleName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["particles"],
    summary="Delete particle",
)
async def delete_particle(
    particleName: str = defaultPath,
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
    tags=["particles"],
    summary="Edit particle",
)
async def edit_particle(
    particleName: str = defaultPath,
    particle: Particle = defaultBody,
) -> None:
    """指定したparticleを編集します"""
    ...


@router.get(
    "/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["particles"],
    summary="Get particle",
)
async def get_particle(
    particleName: str = defaultPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["particles"],
    summary="Get particle list",
)
async def get_particle_list(
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetParticleListResponse:
    """It returns list of particle infos registered in this server.
    Also it can search using query params"""
    ...
