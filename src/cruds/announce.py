from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from src.database.objects.announce import Announce as AnnounceObject
from src.models.announce import Announce as AnnounceModel


async def create_announce(
    db: AsyncSession, announce_create: AnnounceModel
) -> AnnounceObject:
    """お知らせを追加します"""
    announce_date = datetime.now()
    task = AnnounceObject(
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
        user_id=1,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
