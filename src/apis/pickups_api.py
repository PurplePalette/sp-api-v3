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
from src.apis.depends import dependsBody, dependsDatabase, dependsFirebase, dependsPath
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_response import GetLevelResponse
from src.models.pickup import Pickup

router = APIRouter()


@router.post(
    "/pickups",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        409: {"description": "Conflict"},
    },
    tags=["pickups"],
    summary="Add pickup",
)
async def add_pickup(
    pickup: Pickup = dependsBody,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """譜面のピックアップを追加します"""
    ...


@router.delete(
    "/pickups/{pickupName}",
    responses={
        200: {"description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
        409: {"description": "Conflict"},
    },
    tags=["pickups"],
    summary="Delete pickup",
)
async def delete_pickup(
    pickupName: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定したピックアップを削除します"""
    ...


@router.get(
    "/pickups/{pickupName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["pickups"],
    summary="Get pickup",
)
async def get_pickup(
    pickupName: str = dependsPath,
) -> GetLevelResponse:
    """指定されたIDのピックアップを取得して返す"""
    ...
