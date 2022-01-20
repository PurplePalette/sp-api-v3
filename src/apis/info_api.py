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
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.server_info import ServerInfo

router = APIRouter()


@router.get(
    "/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["info"],
    summary="Get server info",
)
async def get_server_info() -> ServerInfo:
    """It returns small list of all infos registered in this server.
    (It should be trimed if the server has too many items)"""
    ...
