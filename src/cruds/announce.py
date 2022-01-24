from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.objects.announce import Announce as AnnounceObject
from src.database.objects.user import User as UserObject
from src.models.announce import Announce as AnnounceModel


async def create_announce(
    db: AsyncSession, announce_create: AnnounceModel, user: FirebaseClaims
) -> AnnounceObject:
    """お知らせを追加します"""
    resp: Result = await db.execute(
        select(UserObject).filter(UserObject.display_id == user["user_id"])
    )
    user_db: Optional[UserObject] = resp.scalars().first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="Specified user was not found")
    announce_date = datetime.now()
    announce = AnnounceObject(
        name=announce_create.announce_name,
        title=announce_create.title,
        title_en="",
        artists=announce_create.subtitle,
        artists_en="",
        author=announce_create.date,
        author_en=announce_create.date,
        description=announce_create.body,
        description_en=announce_create.body,
        public=True,
        created_time=announce_date,
        updated_time=announce_date,
        coverHash=announce_create.resources.icon,
        bgmHash=announce_create.resources.bgm,
        dataHash=announce_create.resources.level,
        user_id=user_db.id,
    )
    db.add(announce)
    await db.commit()
    await db.refresh(announce)
    return announce
