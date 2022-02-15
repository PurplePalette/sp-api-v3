from typing import Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.constraints import LEVEL_VERSION
from src.cruds.constraints import LEVEL_LOCATORS
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    DataBridge,
    get_current_unix,
    get_first_item_or_404,
    is_owner_or_admin_otherwise_409,
    not_exist_or_409,
    patch_to_model,
    save_to_db,
)
from src.database.objects import LevelSave
from src.models.default_search import defaultSearch
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.level import Level as LevelReqResp
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "level"


async def create_level(
    db: AsyncSession, model: LevelReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetLevelResponse]:
    """レベルを追加します"""
    await not_exist_or_409(
        db,
        select(LevelSave).filter(
            LevelSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, LEVEL_LOCATORS, LEVEL_VERSION, auth, True)
    await bridge.to_db(model)
    level_db = LevelSave(**model.dict())
    await save_to_db(db, level_db)
    bridge.to_resp(level_db)
    item = LevelReqResp.from_orm(level_db)
    resp = GetLevelResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_level(db: AsyncSession, name: str, localization: str) -> GetLevelResponse:
    """レベルを取得します"""
    level_db: LevelSave = await get_first_item_or_404(
        db, select(LevelSave).filter(LevelSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, LEVEL_LOCATORS, LEVEL_VERSION)
    bridge.to_resp(level_db, localization)
    item = LevelReqResp.from_orm(level_db)
    return GetLevelResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_level(
    db: AsyncSession,
    name: str,
    model: LevelReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetLevelResponse]:
    """レベルを編集します"""
    level_db: LevelSave = await get_first_item_or_404(
        db,
        select(LevelSave).filter(
            LevelSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, level_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, LEVEL_LOCATORS, LEVEL_VERSION, auth)
    patch_to_model(level_db, model.dict(exclude_unset=True), LEVEL_LOCATORS, [])
    await save_to_db(db, level_db)
    bridge.to_resp(level_db)
    item = LevelReqResp.from_orm(level_db)
    return GetLevelResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_level(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """レベルを削除します"""
    level_db: LevelSave = await get_first_item_or_404(
        db, select(LevelSave).filter(LevelSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, level_db, auth)
    level_db.isDeleted = True
    level_db.updatedTime = get_current_unix()
    save_to_db(db, level_db)
    return None


async def list_level(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetLevelListResponse:
    """レベル一覧を取得します"""
    select_query = buildDatabaseQuery(LevelSave, queries)
    userPage: Page[LevelSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, LEVEL_LOCATORS, LEVEL_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetLevelListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
