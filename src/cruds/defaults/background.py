import asyncio
from typing import Union

from fastapi import HTTPException
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.cruds.defaults.abstract import AbstractCrud
from src.cruds.utils import (
    db_to_resp,
    get_first_item_or_404,
    get_new_name,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.cruds.utils.funcs import remove_prefix
from src.cruds.utils.search import buildDatabaseQuery
from src.cruds.utils.user import is_owner_or_admin_otherwise_409
from src.database.objects.background import Background as BackgroundSave
from src.models.add_background_request import AddBackgroundRequest
from src.models.default_search import defaultSearch
from src.models.edit_background_request import EditBackgroundRequest
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage
from src.security_api import FirebaseClaims


class BackgroundCrud(AbstractCrud):  # type: ignore
    def get_query(self, name: str) -> select:
        """背景を取得するクエリを返します"""
        return (
            select(BackgroundSave)
            .filter(
                BackgroundSave.name == name,
            )
            .options(joinedload(BackgroundSave.user))
        )

    async def get_named_item_or_404(
        self, db: AsyncSession, name: str
    ) -> BackgroundSave:
        """指定した名称の背景が存在すれば取得し、無ければ404を返します"""
        return await get_first_item_or_404(db, self.get_query(name))

    async def add(
        self, db: AsyncSession, model: AddBackgroundRequest, auth: FirebaseClaims
    ) -> Union[HTTPException, GetBackgroundResponse]:
        """背景を追加します"""
        background_db = BackgroundSave(**model.dict())
        background_db.name = await get_new_name(db, BackgroundSave)
        background_db.userId = auth["user_id"]
        await req_to_db(db, background_db, is_new=True)
        await save_to_db(db, background_db)
        # 保存したらリレーションが消し飛ぶので取得し直す
        item = await self.get_named_item_or_404(db, background_db.name)
        await db_to_resp(db, background_db)
        item = background_db.toItem()
        resp = GetBackgroundResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def edit(
        self,
        db: AsyncSession,
        name: str,
        model: EditBackgroundRequest,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, GetBackgroundResponse]:
        """背景を編集します"""
        background_db = await self.get_named_item_or_404(db, name)
        await is_owner_or_admin_otherwise_409(db, background_db, auth)
        patch_to_model(background_db, model.dict(exclude_unset=True))
        await save_to_db(db, background_db)
        # 保存したらリレーションが消し飛ぶので取得し直す
        background_db = await self.get_named_item_or_404(db, background_db.name)
        await db_to_resp(db, background_db)
        item = background_db.toItem()
        return GetBackgroundResponse(
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
        """背景を削除します"""
        await super().delete(db, name, auth)
        return None

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetBackgroundResponse:
        """背景を取得します"""
        background_db = await self.get_named_item_or_404(db, remove_prefix(name))
        await db_to_resp(db, background_db, localization)
        item = background_db.toItem()
        return GetBackgroundResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetBackgroundListResponse:
        """背景一覧を取得します"""
        select_query = buildDatabaseQuery(BackgroundSave, queries, True)
        userPage: Page[BackgroundSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        resp.items = [r.toItem() for r in resp.items]
        return GetBackgroundListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
