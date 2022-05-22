import asyncio
from typing import Union

from fastapi import HTTPException
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from cruds.defaults.defaults_abstract import AbstractCrud
from src.cruds.utils import (
    db_to_resp,
    get_first_item_or_404,
    get_new_name,
    is_owner_or_admin_otherwise_409,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.cruds.utils.search import buildDatabaseQuery
from src.database.objects.skin import Skin as SkinSave
from src.models.add_skin_request import AddSkinRequest
from src.models.default_search import defaultSearch
from src.models.edit_skin_request import EditSkinRequest
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage
from src.security_api import FirebaseClaims


class SkinCrud(AbstractCrud):  # type: ignore
    def get_query(self, name: str) -> select:
        """スキンを取得するクエリを返します"""
        return (
            select(SkinSave)
            .filter(
                SkinSave.name == name,
            )
            .options(joinedload(SkinSave.user))
        )

    async def get_named_item_or_404(self, db: AsyncSession, name: str) -> SkinSave:
        """指定した名称のスキンが存在すれば取得し、無ければ404を返します"""
        return await get_first_item_or_404(db, self.get_query(name))

    async def add(
        self, db: AsyncSession, model: AddSkinRequest, auth: FirebaseClaims
    ) -> Union[HTTPException, GetSkinResponse]:
        """スキンを追加します"""
        skin_db = SkinSave(**model.dict())
        skin_db.name = await get_new_name(db, SkinSave)
        skin_db.userId = auth["user_id"]
        await req_to_db(db, skin_db, is_new=True)
        await save_to_db(db, skin_db)
        skin_db = await self.get_named_item_or_404(db, skin_db.name)
        await db_to_resp(db, skin_db)
        item = skin_db.toItem()
        resp = GetSkinResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def edit(
        self,
        db: AsyncSession,
        name: str,
        model: EditSkinRequest,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, GetSkinResponse]:
        """スキンを編集します"""
        skin_db = await self.get_named_item_or_404(db, name)
        await is_owner_or_admin_otherwise_409(db, skin_db, auth)
        patch_to_model(skin_db, model.dict(exclude_unset=True))
        await save_to_db(db, skin_db)
        await db_to_resp(db, skin_db)
        item = skin_db.toItem()
        return GetSkinResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def delete(
        self,
        db: AsyncSession,
        name: str,
        auth: FirebaseClaims,
    ) -> None:
        """スキンを削除します"""
        await super().delete(db, name, auth)
        return None

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetSkinResponse:
        """スキンを取得します"""
        skin_db = await self.get_named_item_or_404(db, name)
        await db_to_resp(db, skin_db, localization)
        item = skin_db.toItem()
        return GetSkinResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetSkinListResponse:
        """スキン一覧を取得します"""
        select_query = buildDatabaseQuery(SkinSave, queries, True)
        userPage: Page[SkinSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        resp.items = [r.toItem() for r in resp.items]
        return GetSkinListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
