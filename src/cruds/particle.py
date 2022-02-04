from typing import Union

import sqlalchemy  # noqa: F401
from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import PARTICLE_VERSION
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
from src.database.objects.particle import Particle as ParticleSave
from src.models.default_search import defaultSearch
from src.models.particle import Particle as ParticleReqResp
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "particle"
LOCATOR_NAMES = ["thumbnail", "data", "texture"]
OBJECT_VERSION = PARTICLE_VERSION


async def create_particle(
    db: AsyncSession, model: ParticleReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetParticleResponse]:
    """パーティクルセットを追加します"""
    await not_exist_or_409(
        db,
        select(ParticleSave).filter(
            ParticleSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, LOCATOR_NAMES, OBJECT_VERSION, auth, True)
    await bridge.to_db(model)
    particle_db = ParticleSave(**model.dict())
    await save_to_db(db, particle_db)
    bridge.to_resp(particle_db)
    item = ParticleReqResp.from_orm(particle_db)
    resp = GetParticleResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_particle(
    db: AsyncSession, name: str, localization: str
) -> GetParticleResponse:
    """パーティクルセットを取得します"""
    particle_db: ParticleSave = await get_first_item_or_404(
        db, select(ParticleSave).filter(ParticleSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, LOCATOR_NAMES, OBJECT_VERSION)
    bridge.to_resp(particle_db, localization)
    item = ParticleReqResp.from_orm(particle_db)
    return GetParticleResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_particle(
    db: AsyncSession,
    name: str,
    model: ParticleReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetParticleResponse]:
    """パーティクルセットを編集します"""
    particle_db: ParticleSave = await get_first_item_or_404(
        db,
        select(ParticleSave).filter(
            ParticleSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, particle_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, LOCATOR_NAMES, OBJECT_VERSION, auth)
    patch_to_model(particle_db, model.dict(exclude_unset=True), LOCATOR_NAMES, [])
    await save_to_db(db, particle_db)
    bridge.to_resp(particle_db)
    item = ParticleReqResp.from_orm(particle_db)
    return GetParticleResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_particle(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """パーティクルセットを削除します"""
    particle_db: ParticleSave = await get_first_item_or_404(
        db, select(ParticleSave).filter(ParticleSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, particle_db, auth)
    particle_db.isDeleted = True
    particle_db.updatedTime = get_current_unix()
    save_to_db(db, particle_db)
    return None


async def list_particle(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetParticleListResponse:
    """パーティクルセット一覧を取得します"""
    select_query = buildDatabaseQuery(ParticleSave, queries)
    userPage: Page[ParticleSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, LOCATOR_NAMES, OBJECT_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetParticleListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
