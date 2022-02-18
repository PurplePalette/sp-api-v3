import asyncio
from typing import List

from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.abstract import AbstractCrud
from src.cruds.utils import (
    db_to_resp,
    get_admin_or_403,
    get_first_item_or_404,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.database.objects import AnnounceSave
from src.models.add_announce_request import AddAnnounceRequest
from src.models.default_search import defaultSearch
from src.models.edit_announce_request import EditAnnounceRequest
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse


class AnnounceCrud(AbstractCrud):  # type: ignore
    async def add(
        self,
        db: AsyncSession,
        announce_create: AddAnnounceRequest,
        user: FirebaseClaims,
    ) -> GetLevelResponse:
        """お知らせを追加します"""
        announce_db = AnnounceSave(**announce_create.dict())
        announce_db.userId = user["user_id"]
        if announce_db.rating is None:
            announce_db.rating = 1
        await req_to_db(db, announce_db, is_new=True)
        await save_to_db(db, announce_db)
        await db_to_resp(db, announce_db)
        resp: GetLevelResponse = announce_db.toLevelResponse()
        return resp

    async def edit(
        self,
        db: AsyncSession,
        announceName: str,
        announce_edit: EditAnnounceRequest,
        user: FirebaseClaims,
    ) -> GetLevelResponse:
        """お知らせを編集します"""
        await get_admin_or_403(db, user)
        announce_db: AnnounceSave = await get_first_item_or_404(
            db, select(AnnounceSave).filter(AnnounceSave.name == announceName)
        )
        patch_to_model(announce_db, announce_edit.dict(exclude_unset=True))
        await save_to_db(db, announce_db)
        await db_to_resp(db, announce_db)
        resp: GetLevelResponse = announce_db.toLevelResponse()
        return resp

    async def delete(
        self,
        db: AsyncSession,
        announceName: str,
        user: FirebaseClaims,
    ) -> None:
        """お知らせを削除します"""
        await get_admin_or_403(db, user)
        announce_db: AnnounceSave = await get_first_item_or_404(
            db, select(AnnounceSave).filter(AnnounceSave.name == announceName)
        )
        await db.delete(announce_db)
        await db.commit()

    async def get(
        self,
        db: AsyncSession,
        announceName: str,
    ) -> GetLevelResponse:
        """お知らせを取得します"""
        announce_db: AnnounceSave = await get_first_item_or_404(
            db, select(AnnounceSave).filter(AnnounceSave.name == announceName)
        )
        await db_to_resp(db, announce_db)
        resp: GetLevelResponse = announce_db.toLevelResponse()
        return resp

    async def list(
        self,
        db: AsyncSession,
    ) -> GetLevelListResponse:
        """お知らせ一覧を取得します"""
        resp: Result = await db.execute(
            select(AnnounceSave).order_by(AnnounceSave.updatedTime.desc())
        )
        announces: List[AnnounceSave] = resp.scalars()
        await asyncio.gather(*[db_to_resp(db, announce) for announce in announces])
        return GetLevelListResponse(
            pageCount=1,
            items=[announce.toLevelItem() for announce in announces],
            search=defaultSearch,
        )
