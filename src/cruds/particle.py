import asyncio
from typing import Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.abstract import AbstractCrud
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    db_to_resp,
    get_current_unix,
    get_first_item_or_404,
    get_new_name,
    is_owner_or_admin_otherwise_409,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.database.objects import ParticleSave
from src.models.default_search import defaultSearch
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.particle import Particle as ParticleReqResp
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage


class ParticleCrud(AbstractCrud):
    async def add(
        self, db: AsyncSession, model: ParticleReqResp, auth: FirebaseClaims
    ) -> Union[HTTPException, GetParticleResponse]:
        """パーティクルセットを追加します"""
        particle_db = ParticleSave(**model.dict())
        particle_db.name = await get_new_name(db, ParticleSave)
        particle_db.userId = auth["user_id"]
        await req_to_db(db, particle_db, is_new=True)
        await save_to_db(db, particle_db)
        await db_to_resp(db, particle_db)
        item = ParticleReqResp.from_orm(particle_db)
        resp = GetParticleResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetParticleResponse:
        """パーティクルセットを取得します"""
        particle_db: ParticleSave = await get_first_item_or_404(
            db, select(ParticleSave).filter(ParticleSave.name == name)
        )
        await db_to_resp(db, particle_db, localization)
        item = ParticleReqResp.from_orm(particle_db)
        return GetParticleResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def edit(
        self,
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
        patch_to_model(particle_db, model.dict(exclude_unset=True))
        await save_to_db(db, particle_db)
        await db_to_resp(db, particle_db)
        item = ParticleReqResp.from_orm(particle_db)
        return GetParticleResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def delete(
        self,
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
        await save_to_db(db, particle_db)
        return None

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetParticleListResponse:
        """パーティクルセット一覧を取得します"""
        select_query = buildDatabaseQuery(ParticleSave, queries)
        userPage: Page[ParticleSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        return GetParticleListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
