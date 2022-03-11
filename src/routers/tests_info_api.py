# coding: utf-8

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.tests.info import TestInfoCrud
from src.models.server_info import ServerInfo
from src.routers.depends import dependsDatabase, dependsLocalization, dependsPath

router = APIRouter()
crud = TestInfoCrud()


@router.get(
    "/tests/{testId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["tests_info"],
    summary="Get test server info",
)
async def get_test_server_info(
    db: AsyncSession = dependsDatabase,
    testId: str = dependsPath,
    localization: str = dependsLocalization,
) -> ServerInfo:
    """テスト個別の情報一覧を返します"""
    return await crud.list_info(db, testId, localization)
