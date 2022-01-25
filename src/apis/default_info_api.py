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
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import dependsDatabase
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.server_info import ServerInfo

router = APIRouter()


@router.get(
    "/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["default_info"],
    summary="Get default server info",
)
async def get_server_info(
    db: AsyncSession = dependsDatabase,
) -> ServerInfo:
    """It returns small list of all infos registered in this server.
    (It should be trimmed if the server has too many items)"""
    ...
