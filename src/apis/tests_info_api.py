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
from src.apis.depends import dependsPath
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.server_info import ServerInfo

router = APIRouter()


@router.get(
    "/tests/{testId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["tests_info"],
    summary="Get test server info",
)
async def get_test_server_info(
    testId: str = dependsPath,
) -> ServerInfo:
    """テスト個別の情報一覧を返します"""
    ...
