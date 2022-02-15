from typing import Union

import sqlalchemy  # noqa: F401
from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.constraints import SKIN_VERSION
from src.cruds.constraints import SKIN_LOCATORS
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
from src.database.objects import SkinSave
from src.models.default_search import defaultSearch
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchQueries
from src.models.skin import Skin as SkinReqResp
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "skin"


async def create_skin(
    db: AsyncSession, model: SkinReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetSkinResponse]:
    """スキンを追加します"""
    await not_exist_or_409(
        db,
        select(SkinSave).filter(
            SkinSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, SKIN_LOCATORS, SKIN_VERSION, auth, True)
    await bridge.to_db(model)
    skin_db = SkinSave(**model.dict())
    await save_to_db(db, skin_db)
    bridge.to_resp(skin_db)
    item = SkinReqResp.from_orm(skin_db)
    resp = GetSkinResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_skin(db: AsyncSession, name: str, localization: str) -> GetSkinResponse:
    """スキンを取得します"""
    skin_db: SkinSave = await get_first_item_or_404(
        db, select(SkinSave).filter(SkinSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, SKIN_LOCATORS, SKIN_VERSION)
    bridge.to_resp(skin_db, localization)
    item = SkinReqResp.from_orm(skin_db)
    return GetSkinResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_skin(
    db: AsyncSession,
    name: str,
    model: SkinReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetSkinResponse]:
    """スキンを編集します"""
    skin_db: SkinSave = await get_first_item_or_404(
        db,
        select(SkinSave).filter(
            SkinSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, skin_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, SKIN_LOCATORS, SKIN_VERSION, auth)
    patch_to_model(skin_db, model.dict(exclude_unset=True), SKIN_LOCATORS, [])
    await save_to_db(db, skin_db)
    bridge.to_resp(skin_db)
    item = SkinReqResp.from_orm(skin_db)
    return GetSkinResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_skin(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """スキンを削除します"""
    skin_db: SkinSave = await get_first_item_or_404(
        db, select(SkinSave).filter(SkinSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, skin_db, auth)
    skin_db.isDeleted = True
    skin_db.updatedTime = get_current_unix()
    save_to_db(db, skin_db)
    return None


async def list_skin(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetSkinListResponse:
    """スキン一覧を取得します"""
    select_query = buildDatabaseQuery(SkinSave, queries)
    userPage: Page[SkinSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, SKIN_LOCATORS, SKIN_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetSkinListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
