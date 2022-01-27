from datetime import datetime
from typing import List

from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils import get_admin_or_403, get_first_item_or_404, not_exist_or_409
from src.database.objects.announce import Announce as AnnounceObject
from src.models.announce import Announce as AnnounceModel


async def create_announce(
    db: AsyncSession, announce_create: AnnounceModel, user: FirebaseClaims
) -> None:
    """お知らせを追加します"""
    user_db = await get_admin_or_403(db, user)
    await not_exist_or_409(
        db,
        select(AnnounceObject).filter(AnnounceObject.name == announce_create.name),
    )
    announce_date = datetime.now()
    announce = AnnounceObject(
        name=announce_create.name,
        title=announce_create.title,
        title_en=announce_create.title,
        artists=announce_create.subtitle,
        artists_en=announce_create.subtitle,
        author=announce_create.date,
        author_en=announce_create.date,
        description=announce_create.body,
        description_en=announce_create.body,
        public=True,
        created_time=announce_date,
        updated_time=announce_date,
        cover_hash=announce_create.resources.icon,
        bgm_hash=announce_create.resources.bgm,
        data_hash=announce_create.resources.level,
        user_id=user_db.id,
    )
    db.add(announce)
    await db.commit()
    await db.refresh(announce)


async def edit_announce(
    db: AsyncSession,
    announceName: str,
    announce_edit: AnnounceModel,
    user: FirebaseClaims,
) -> None:
    """お知らせを編集します"""
    user_db = await get_admin_or_403(db, user)
    announce_db: AnnounceObject = await get_first_item_or_404(
        db, select(AnnounceObject).filter(AnnounceObject.name == announceName)
    )
    update_data = announce_edit.dict(exclude_unset=True)
    for k in update_data.keys():
        if k == "name":
            announce_db.name = update_data[k]
        elif k == "title":
            announce_db.title = update_data[k]
            announce_db.title_en = update_data[k]
        elif k == "subtitle":
            announce_db.artists = update_data[k]
            announce_db.artists_en = update_data[k]
        elif k == "date":
            announce_db.author = update_data[k]
            announce_db.author_en = update_data[k]
        elif k == "body":
            announce_db.description = update_data[k]
            announce_db.description_en = update_data[k]
        elif k == "resources":
            for r in update_data[k].keys():
                if r == "icon":
                    announce_db.cover_hash = update_data[k][r]
                elif r == "bgm":
                    announce_db.bgm_hash = update_data[k][r]
                elif r == "level":
                    announce_db.data_hash = update_data[k][r]
    announce_db.user = user_db
    announce_db.updated_time = datetime.now()
    db.add(announce_db)
    await db.commit()
    await db.refresh(announce_db)


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
) -> AnnounceObject:
    """お知らせを取得します"""
    announce_db: AnnounceObject = await get_first_item_or_404(
        db, select(AnnounceObject).filter(AnnounceObject.name == announceName)
    )
    return announce_db


async def list_announce(
    db: AsyncSession,
) -> List[AnnounceObject]:
    """お知らせ一覧を取得します"""
    resp: Result = await db.execute(
        select(AnnounceObject).order_by(AnnounceObject.updated_time.desc())
    )
    announces: List[AnnounceObject] = resp.scalars()
    return announces
