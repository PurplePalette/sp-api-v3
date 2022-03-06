from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.objects.user import User


async def get_internal_id(db: AsyncSession, userId: str) -> int:
    """指定された表示ID(FirebaseID)のユーザーのデータベース内部IDを取得"""
    user = await db.execute(select(User.id).filter(User.userId == userId))
    res: Optional[int] = user.scalars().first()
    if res is None:
        raise HTTPException(
            status_code=401, detail="Your account is not registered in this server"
        )
    return res


async def get_display_id(db: AsyncSession, id: int) -> str:
    """指定された内部ID(データベースID)のユーザーの表示ID(FirebaseID)を取得"""
    user = await db.execute(select(User.userId).filter(User.id == id))
    res: Optional[str] = user.scalars().first()
    if res is None:
        raise Exception("Your account is not registered in this server")
    return res
