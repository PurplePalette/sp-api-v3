from abc import ABCMeta
from typing import Any, Optional, TypeVar

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils.funcs import get_random_name


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
