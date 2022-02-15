from dataclasses import dataclass
from typing import Any, Dict, List, Union  # noqa: F401

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.constraints import ENGINE_LOCATORS, ENGINE_VERSION
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    DataBridge,
    all_fields_exists_or_400,
    get_current_unix,
    get_first_item_or_404,
    is_owner_or_admin_otherwise_409,
    not_exist_or_409,
    patch_to_model,
    save_to_db,
)
from src.database.objects import (  # noqa: F401
    BackgroundSave,
    EffectSave,
    EngineSave,
    ParticleSave,
    SkinSave,
)
from src.models.default_search import defaultSearch
from src.models.engine import Engine as EngineReqResp
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "engine"


@dataclass
class ModelKeyNameValue:
    key: Any
    value: str


async def create_engine(
    db: AsyncSession, model: EngineReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetEngineResponse]:
    """エンジンを追加します"""
    await not_exist_or_409(
        db,
        select(EngineSave).filter(
            EngineSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, ENGINE_LOCATORS, ENGINE_VERSION, auth, True)
    await bridge.to_db(model)
    # 必須パラメータの存在確認
    all_fields_exists_or_400(
        [model.skin, model.particle, model.effect, model.background]
    )
    all_fields_exists_or_400(
        [model.skin.name, model.particle.name, model.effect.name, model.background.name]
    )
    # Skin/Particle/Effect/Backgroundをnameから召喚
    models: List[ModelKeyNameValue] = [
        ModelKeyNameValue(key=SkinSave, value=model.skin.name),
        ModelKeyNameValue(key=ParticleSave, value=model.particle.name),
        ModelKeyNameValue(key=EffectSave, value=model.effect.name),
        ModelKeyNameValue(key=BackgroundSave, value=model.background.name),
    ]
    for model in models:
        item = await get_first_item_or_404(
            db, select(model.key).filter(model.key.name == model.value)
        )
        setattr(model, model.key, item)

    engine_db = EngineSave(**model.dict())
    await save_to_db(db, engine_db)
    bridge.to_resp(engine_db)
    item = EngineReqResp.from_orm(engine_db)
    resp = GetEngineResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_engine(
    db: AsyncSession, name: str, localization: str
) -> GetEngineResponse:
    """エンジンを取得します"""
    engine_db: EngineSave = await get_first_item_or_404(
        db, select(EngineSave).filter(EngineSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, ENGINE_LOCATORS, ENGINE_VERSION)
    bridge.to_resp(engine_db, localization)
    item = EngineReqResp.from_orm(engine_db)
    return GetEngineResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_engine(
    db: AsyncSession,
    name: str,
    model: EngineReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetEngineResponse]:
    """エンジンを編集します"""
    engine_db: EngineSave = await get_first_item_or_404(
        db,
        select(EngineSave).filter(
            EngineSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, engine_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, ENGINE_LOCATORS, ENGINE_VERSION, auth)
    patch_to_model(engine_db, model.dict(exclude_unset=True), ENGINE_LOCATORS, [])
    await save_to_db(db, engine_db)
    bridge.to_resp(engine_db)
    item = EngineReqResp.from_orm(engine_db)
    return GetEngineResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_engine(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """エンジンを削除します"""
    engine_db: EngineSave = await get_first_item_or_404(
        db, select(EngineSave).filter(EngineSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, engine_db, auth)
    engine_db.isDeleted = True
    engine_db.updatedTime = get_current_unix()
    save_to_db(db, engine_db)
    return None


async def list_engine(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetEngineListResponse:
    """エンジン一覧を取得します"""
    select_query = buildDatabaseQuery(EngineSave, queries)
    userPage: Page[EngineSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, ENGINE_LOCATORS, ENGINE_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetEngineListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
