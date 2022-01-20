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
from src.models.engine import Engine
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse


router = APIRouter()


@router.post(
    "/engines",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["engines"],
    summary="Add engine",
)
async def add_engine(
    engine: Engine = Body(None, description=""),
) -> None:
    """指定されたゲームエンジンをサーバーに登録します"""
    ...


@router.delete(
    "/engines/{engineName}",
    responses={
        200: {"description": "OK"},
    },
    tags=["engines"],
    summary="Delete Engine",
)
async def delete_engine(
    engineName: str = Path(None, description=""),
) -> None:
    """delete a engine"""
    ...


@router.patch(
    "/engines/{engineName}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["engines"],
    summary="Edit engine",
)
async def edit_engine(
    engineName: str = Path(None, description=""),
    engine: Engine = Body(None, description=""),
) -> None:
    """指定されたengineを編集します"""
    ...


@router.get(
    "/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["engines"],
    summary="Get engine",
)
async def get_engine(
    engineName: str = Path(None, description=""),
) -> GetEngineResponse:
    """It returns specified engine info It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
    },
    tags=["engines"],
    summary="Get engine list",
)
async def get_engine_list(
    localization: str = Query(None, description="It localizes response items if possible", min_length=1, max_length=50),
    page: int = Query(1, description="It filters items for pagination if possible", ge=0, le=10000),
    keywords: str = Query(None, description="It filters items for search from list if possible", min_length=1, max_length=300),
) -> GetEngineListResponse:
    """It returns list of engine infos registered in this server Also it can search using query params"""
    ...
