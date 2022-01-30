from typing import List

from fastapi_cloudauth.firebase import FirebaseClaims
from src.models.get_level_response import GetLevelResponse
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils import (
    get_admin_or_403,
    get_current_unix,
    get_first_item_or_404,
    not_exist_or_409,
)
from src.database.objects.announce import Announce as AnnounceObject
from src.models.announce import Announce as AnnounceModel
from src.models.default_search import defaultSearch
from src.models.get_level_list_response import GetLevelListResponse
from src.models.sonolus_resource_locator import SonolusResourceLocator


async def create_announce(
    db: AsyncSession, announce_create: AnnounceModel, user: FirebaseClaims
) -> GetLevelResponse:
    """お知らせを追加します"""
    user_db = await get_admin_or_403(db, user)
    await not_exist_or_409(
        db,
        select(AnnounceObject).filter(AnnounceObject.name == announce_create.name),
    )
    announce_db = AnnounceObject(**announce_create.dict())
    announce_db.user = user_db
    announce_db.createdTime = get_current_unix()
    announce_db.updatedTime = get_current_unix()
    announce_db.cover = announce_create.cover.hash
    announce_db.bgm = announce_create.bgm.hash
    announce_db.preview = announce_create.preview.hash
    db.add(announce_db)
    await db.commit()
    await db.refresh(announce_db)
    resp: GetLevelResponse = announce_db.toLevelResponse()
    return resp


async def edit_announce(
    db: AsyncSession,
    announceName: str,
    announce_edit: AnnounceModel,
    user: FirebaseClaims,
) -> GetLevelResponse:
    """お知らせを編集します"""
    user_db = await get_admin_or_403(db, user)
    announce_db: AnnounceObject = await get_first_item_or_404(
        db, select(AnnounceObject).filter(AnnounceObject.name == announceName)
    )
    update_data = announce_edit.dict(exclude_unset=True)
    update_data["userId"] = user_db.id
    update_data["createdTime"] = announce_db.createdTime
    update_data["updatedTime"] = get_current_unix()
    if "cover" in update_data:
        update_data["cover"] = announce_edit.cover.hash
    if "bgm" in update_data:
        update_data["bgm"] = announce_edit.bgm.hash
    if "preview" in update_data:
        update_data["preview"] = announce_edit.preview.hash
    for key, value in update_data.items():
        setattr(announce_db, key, value)
    db.add(announce_db)
    await db.commit()
    await db.refresh(announce_db)
    announce_db.cover = SonolusResourceLocator(
        type="LevelCover", hash=announce_db.cover, url="a"
    )
    announce_db.bgm = SonolusResourceLocator(
        type="LevelBgm", hash=announce_db.bgm, url="a"
    )
    announce_db.preview = SonolusResourceLocator(
        type="LevelPreview", hash=announce_db.preview, url="a"
    )
    resp: GetLevelResponse = announce_db.toLevelResponse()
    return resp


async def delete_announce(
    db: AsyncSession,
    announceName: str,
    user: FirebaseClaims,
) -> None:
    """お知らせを削除します"""
    await get_admin_or_403(db, user)
    announce_db: AnnounceObject = await get_first_item_or_404(
        db, select(AnnounceObject).filter(AnnounceObject.name == announceName)
    )
    await db.delete(announce_db)
    await db.commit()


async def get_announce(
    db: AsyncSession,
    announceName: str,
) -> GetLevelResponse:
    """お知らせを取得します"""
    announce_db: AnnounceObject = await get_first_item_or_404(
        db, select(AnnounceObject).filter(AnnounceObject.name == announceName)
    )
    resp: GetLevelResponse = announce_db.toLevelResponse()
    return resp


async def list_announce(
    db: AsyncSession,
) -> GetLevelListResponse:
    """お知らせ一覧を取得します"""
    resp: Result = await db.execute(
        select(AnnounceObject).order_by(AnnounceObject.updatedTime.desc())
    )
    announces: List[AnnounceObject] = resp.scalars()
    return GetLevelListResponse(
        pageCount=1,
        items=[announce.toLevelItem() for announce in announces],
        search=defaultSearch,
    )
