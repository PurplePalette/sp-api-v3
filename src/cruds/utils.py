import asyncio
import time
from abc import ABCMeta
from typing import Any, Optional, TypeVar

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import func, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true
from src.database.objects.background import Background
from src.database.objects.effect import Effect
from src.database.objects.engine import Engine
from src.database.objects.level import Level
from src.database.objects.particle import Particle
from src.database.objects.skin import Skin
from src.database.objects.user import User as UserObject
from src.models.user_total_publish import UserTotalPublish


class MustHaveName(metaclass=ABCMeta):
    """名前を持つオブジェクトを表す基底クラス"""

    name: str


T = TypeVar("T", bound=MustHaveName)


class MustHaveUserId(metaclass=ABCMeta):
    """ユーザーIDを持つオブジェクトを表す基底クラス"""

    userId: str


U = TypeVar("U", bound=MustHaveUserId)


def get_current_unix() -> int:
    """現在のUNIX時刻を取得"""
    return int(time.time())


async def get_first_item_or_error(
    db: AsyncSession, statement: Any, error: HTTPException
) -> T:
    """データベースに指定された要素が存在すれば取得、なければエラー"""
    resp: Result = await db.execute(statement)
    obj_db: Optional[T] = resp.scalars().first()
    if obj_db is None:
        raise error
    return obj_db


async def get_first_item_or_404(
    db: AsyncSession,
    statement: Any,
) -> T:
    """データベースに指定された要素が存在すれば取得、なければ NotFound"""
    resp: T = await get_first_item_or_error(
        db, statement, HTTPException(status_code=404, detail="Not found")
    )
    return resp


async def get_first_item_or_403(
    db: AsyncSession,
    statement: Any,
) -> T:
    """データベースに指定された要素が存在すれば取得、なければ Forbidden"""
    resp: T = await get_first_item_or_error(
        db, statement, HTTPException(status_code=403, detail="Forbidden")
    )
    return resp


async def get_user_or_404(
    db: AsyncSession,
    user: FirebaseClaims,
) -> UserObject:
    """データベースに指定されたユーザーが存在すれば取得、なければ NotFound"""
    user_db: UserObject = await get_first_item_or_404(
        db, select(UserObject).filter(UserObject.userId == user["user_id"])
    )
    return user_db


async def get_admin_or_403(
    db: AsyncSession,
    user: FirebaseClaims,
) -> UserObject:
    """データベースに指定された管理者ユーザーが存在すれば取得、なければ Forbidden"""
    user_db: UserObject = await get_first_item_or_403(
        db,
        select(UserObject).filter(
            UserObject.userId == user["user_id"], UserObject.isAdmin == true()
        ),
    )
    return user_db


async def not_exist_or_409(db: AsyncSession, statement: Any) -> None:
    """データベースに指定された要素が存在すれば Conflict"""
    resp: Result = await db.execute(statement)
    obj_db: bool = resp.scalars().first()
    if obj_db:
        raise HTTPException(status_code=409, detail="Conflict")


async def is_owner_or_admin_otherwise_409(
    db: AsyncSession, model: U, auth: FirebaseClaims
) -> None:
    """認証ユーザーが本人または管理者でなければ Forbidden"""
    if model.userId != auth["user_id"]:
        await get_admin_or_403(db, auth)


async def get_total_publish(db: AsyncSession, databaseId: int) -> UserTotalPublish:
    """指定された内部ユーザーIDのユーザーの各要素の投稿数を取得"""
    counts = await asyncio.gather(
        *[
            db.execute(
                select([func.count(obj.id)]).filter(
                    obj.userId == databaseId and obj.public == true()
                )
            )
            for obj in [Background, Effect, Engine, Particle, Level, Skin]
        ]
    )
    results = list(map(lambda c: int(c.scalars().first()), counts))
    return UserTotalPublish(
        backgrounds=results[0],
        effects=results[1],
        engines=results[2],
        particles=results[3],
        levels=results[4],
        skins=results[5],
    )


async def get_internal_id(db: AsyncSession, userId: str) -> int:
    """指定された表示ID(FirebaseID)のユーザーのデータベース内部IDを取得"""
    user: UserObject = await db.execute(
        select(UserObject.id).filter(UserObject.userId == userId)
    )
    res: int = user.scalars().first()
    return res
