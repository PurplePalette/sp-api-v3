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
from src.database.objects import EffectSave
from src.models.default_search import defaultSearch
from src.models.effect import Effect as EffectReqResp
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage


class EffectCrud(AbstractCrud):  # type: ignore
    async def add(
        self, db: AsyncSession, model: EffectReqResp, auth: FirebaseClaims
    ) -> Union[HTTPException, GetEffectResponse]:
        """効果音セットを追加します"""
        effect_db = EffectSave(**model.dict())
        effect_db.name = await get_new_name(db, EffectSave)
        effect_db.userId = auth["user_id"]
        await req_to_db(db, effect_db, is_new=True)
        await save_to_db(db, effect_db)
        await db_to_resp(db, effect_db)
        item = EffectReqResp.from_orm(effect_db)
        resp = GetEffectResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetEffectResponse:
        """効果音セットを取得します"""
        effect_db: EffectSave = await get_first_item_or_404(
            db, select(EffectSave).filter(EffectSave.name == name)
        )
        await db_to_resp(db, effect_db, localization)
        item = EffectReqResp.from_orm(effect_db)
        return GetEffectResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def edit(
        self,
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
        patch_to_model(effect_db, model.dict(exclude_unset=True))
        await save_to_db(db, effect_db)
        await db_to_resp(db, effect_db)
        item = EffectReqResp.from_orm(effect_db)
        return GetEffectResponse(
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
        """効果音セットを削除します"""
        effect_db: EffectSave = await get_first_item_or_404(
            db, select(EffectSave).filter(EffectSave.name == name)
        )
        await is_owner_or_admin_otherwise_409(db, effect_db, auth)
        effect_db.isDeleted = True
        effect_db.updatedTime = get_current_unix()
        await save_to_db(db, effect_db)
        return None

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetEffectListResponse:
        """効果音セット一覧を取得します"""
        select_query = buildDatabaseQuery(EffectSave, queries)
        userPage: Page[EffectSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        return GetEffectListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
