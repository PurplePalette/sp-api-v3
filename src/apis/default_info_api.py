# coding: utf-8
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import dependsDatabase, dependsLocalization
from src.cruds.defaults.info import list_info
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
    db: AsyncSession = dependsDatabase, localization: str = dependsLocalization
) -> ServerInfo:
    """It returns small list of all infos registered in this server.
    (It should be trimmed if the server has too many items)"""
    return await list_info(db, localization)
