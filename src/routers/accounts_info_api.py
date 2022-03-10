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
    "/accounts/{accountKey}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["accounts_info"],
    summary="Get account server info",
)
async def get_accounts_server_info(
    accountKey: str = dependsPath,
) -> ServerInfo:
    """ユーザー個別の情報一覧を返します"""
    ...
