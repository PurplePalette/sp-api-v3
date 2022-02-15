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
from src.database.objects import SkinSave
from src.models.add_skin_request import AddSkinRequest
from src.models.default_search import defaultSearch
from src.models.edit_skin_request import EditSkinRequest
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchQueries
from src.models.skin import Skin as SkinReqResp
from src.models.sonolus_page import SonolusPage, toSonolusPage


class SkinCrud(AbstractCrud):  # type: ignore
    async def add(
        self, db: AsyncSession, model: AddSkinRequest, auth: FirebaseClaims
    ) -> Union[HTTPException, GetSkinResponse]:
        """スキンを追加します"""
        skin_db = SkinSave(**model.dict())
        skin_db.name = await get_new_name(db, SkinSave)
        skin_db.userId = auth["user_id"]
        await req_to_db(db, skin_db, is_new=True)
        await save_to_db(db, skin_db)
        await db_to_resp(db, skin_db)
        item = SkinReqResp.from_orm(skin_db)
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
        skin_db: SkinSave = await get_first_item_or_404(
            db,
            select(SkinSave).filter(
                SkinSave.name == name,
            ),
        )
        await is_owner_or_admin_otherwise_409(db, skin_db, auth)
        patch_to_model(skin_db, model.dict(exclude_unset=True))
        await save_to_db(db, skin_db)
        await db_to_resp(db, skin_db)
        item = SkinReqResp.from_orm(skin_db)
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
    ) -> Union[HTTPException, None]:
        """スキンを削除します"""
        skin_db: SkinSave = await get_first_item_or_404(
            db, select(SkinSave).filter(SkinSave.name == name)
        )
        await is_owner_or_admin_otherwise_409(db, skin_db, auth)
        skin_db.isDeleted = True
        skin_db.updatedTime = get_current_unix()
        await save_to_db(db, skin_db)
        return None

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetSkinResponse:
        """スキンを取得します"""
        skin_db: SkinSave = await get_first_item_or_404(
            db, select(SkinSave).filter(SkinSave.name == name)
        )
        await db_to_resp(db, skin_db, localization)
        item = SkinReqResp.from_orm(skin_db)
        return GetSkinResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetSkinListResponse:
        """スキン一覧を取得します"""
        select_query = buildDatabaseQuery(SkinSave, queries)
        userPage: Page[SkinSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        return GetSkinListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
