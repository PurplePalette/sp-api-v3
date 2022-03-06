from abc import ABCMeta
from typing import Any, Optional, TypeVar

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true
from src.cruds.utils.funcs import get_random_name
from src.database.objects.user import User as UserObject


class MustHaveName(metaclass=ABCMeta):
    """名前を持つオブジェクトを表す基底クラス"""

    name: str


T = TypeVar("T", bound=MustHaveName)


class MustHaveUserId(metaclass=ABCMeta):
    """ユーザーIDを持つオブジェクトを表す基底クラス"""

    userId: str


U = TypeVar("U", bound=MustHaveUserId)


def get_first_item(db: AsyncSession, statement: Any) -> Optional[T]:
    """データベースに指定された要素が存在すれば取得"""
    resp: Result = db.execute(statement)
    obj_db: Optional[T] = resp.scalars().first()
    return obj_db


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
        db,
        statement,
        HTTPException(
            status_code=404, detail="Specified content was not found on server"
        ),
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


async def is_exist(db: AsyncSession, statement: Any) -> bool:
    """指定した要素が存在するかBoolで返す"""
    resp: Result = await db.execute(statement)
    obj_db: Optional[Any] = resp.scalars().first()
    return True if obj_db else False


async def is_owner_or_admin_otherwise_409(
    db: AsyncSession, model: U, auth: FirebaseClaims
) -> None:
    """認証ユーザーが本人または管理者でなければ Forbidden"""
    if model.userId != auth["user_id"]:
        await get_admin_or_403(db, auth)


async def get_new_name(db: AsyncSession, obj: T) -> str:
    """指定されたObjectの、既存のデータと衝突しない新しいnameを生成"""
    existed = True
    newName = ""
    while existed:
        newName = get_random_name()
        existed = await is_exist(
            db,
            select(obj).filter(
                obj.name == newName,
            ),
        )
    return newName


async def save_to_db(db: AsyncSession, model: Any) -> Optional[HTTPException]:
    """データベースにモデルを追加/反映するショートハンド"""
    db.add(model)
    try:
        await db.commit()
        await db.refresh(model)
    except IntegrityError as e:
        if "Duplicate entry" in e._message():
            return HTTPException(status_code=409, detail="Conflicted")
        return HTTPException(status_code=400, detail="Bad Request")
    return None
