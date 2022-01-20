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
from src.apis.defaults import defaultBody, defaultPath
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_response import GetLevelResponse
from src.models.pickup import Pickup

router = APIRouter()


@router.post(
    "/pickups",
    responses={
        200: {"description": "OK"},
    },
    tags=["pickups"],
    summary="Add Pickup",
)
async def add_pickup(
    pickup: Pickup = defaultBody,
) -> None:
    """譜面のピックアップを追加します"""
    ...


@router.delete(
    "/pickups/{pickupName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["pickups"],
    summary="Delete pickup",
)
async def delete_pickup(
    pickupName: str = defaultPath,
    pickup: Pickup = defaultBody,
) -> None:
    """指定したピックアップを削除します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/fresh-release",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["pickups"],
    summary="Get pickups",
)
async def get_account_fresh_levels(
    accountKey: str = defaultPath,
) -> GetLevelResponse:
    """新規譜面作者の譜面のみを返すエンドポイント"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/pickups",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["pickups"],
    summary="Get pickups",
)
async def get_account_pickup_levels(
    accountKey: str = defaultPath,
) -> GetLevelResponse:
    """管理者の指定したおすすめ譜面などを返すエンドポイント"""
    ...


@router.get(
    "/pickups/{pickupName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["pickups"],
    summary="Get pickup",
)
async def get_pickup(
    pickupName: str = defaultPath,
) -> GetLevelResponse:
    """指定されたIDのピックアップを取得して返す"""
    ...
