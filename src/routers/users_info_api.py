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
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.server_info import ServerInfo
from src.routers.depends import dependsPath

router = APIRouter()


@router.get(
    "/users/{userId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["users_info"],
    summary="Get user server info",
)
async def get_user_server_info(
    userId: str = dependsPath,
) -> ServerInfo:
    """ユーザー個別の情報一覧を返します"""
    ...
