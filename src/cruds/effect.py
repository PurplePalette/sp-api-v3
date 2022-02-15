from typing import Union

import sqlalchemy  # noqa: F401
from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.constraints import EFFECT_VERSION
from src.cruds.constraints import EFFECT_LOCATORS
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
from src.database.objects import EffectSave
from src.models.default_search import defaultSearch
from src.models.effect import Effect as EffectReqResp
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "effect"


async def create_effect(
    db: AsyncSession, model: EffectReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetEffectResponse]:
    """効果音セットを追加します"""
    await not_exist_or_409(
        db,
        select(EffectSave).filter(
            EffectSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, EFFECT_LOCATORS, EFFECT_VERSION, auth, True)
    await bridge.to_db(model)
    effect_db = EffectSave(**model.dict())
    await save_to_db(db, effect_db)
    bridge.to_resp(effect_db)
    item = EffectReqResp.from_orm(effect_db)
    resp = GetEffectResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_effect(
    db: AsyncSession, name: str, localization: str
) -> GetEffectResponse:
    """効果音セットを取得します"""
    effect_db: EffectSave = await get_first_item_or_404(
        db, select(EffectSave).filter(EffectSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, EFFECT_LOCATORS, EFFECT_VERSION)
    bridge.to_resp(effect_db, localization)
    item = EffectReqResp.from_orm(effect_db)
    return GetEffectResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_effect(
    db: AsyncSession,
    name: str,
    model: EffectReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetEffectResponse]:
    """効果音セットを編集します"""
    effect_db: EffectSave = await get_first_item_or_404(
        db,
        select(EffectSave).filter(
            EffectSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, effect_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, EFFECT_LOCATORS, EFFECT_VERSION, auth)
    patch_to_model(effect_db, model.dict(exclude_unset=True), EFFECT_LOCATORS, [])
    await save_to_db(db, effect_db)
    bridge.to_resp(effect_db)
    item = EffectReqResp.from_orm(effect_db)
    return GetEffectResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_effect(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """効果音セットを削除します"""
    effect_db: EffectSave = await get_first_item_or_404(
        db, select(EffectSave).filter(EffectSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, effect_db, auth)
    effect_db.isDeleted = True
    effect_db.updatedTime = get_current_unix()
    save_to_db(db, effect_db)
    return None


async def list_effect(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetEffectListResponse:
    """効果音セット一覧を取得します"""
    select_query = buildDatabaseQuery(EffectSave, queries)
    userPage: Page[EffectSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, EFFECT_LOCATORS, EFFECT_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetEffectListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
