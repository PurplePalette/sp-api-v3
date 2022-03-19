# coding: utf-8

from fastapi import APIRouter
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.users.info import UserInfoCrud
from src.models.server_info import ServerInfo
from src.routers.depends import dependsDatabase, dependsLocalization, dependsPath

router = APIRouter()
crud = UserInfoCrud()


@router.get(
    "/users/{userId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["users_info"],
    summary="Get user server info",
)
async def get_user_server_info(
    db: AsyncSession = dependsDatabase,
    userId: str = dependsPath,
    localization: str = dependsLocalization,
) -> ServerInfo:
    """テスト個別の情報一覧を返します"""
    return await crud.list_info(db, userId, localization)


@router.get("/users/{userId}/index")
def users_index() -> FileResponse:
    return FileResponse("src/static/server.html")
