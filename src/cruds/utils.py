import asyncio
import time
from abc import ABCMeta
from typing import Any, Dict, List, Optional, TypeVar, Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import func, select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true
from src.config import CDN_ENDPOINT
from src.database.objects.background import Background
from src.database.objects.effect import Effect
from src.database.objects.engine import Engine
from src.database.objects.level import Level
from src.database.objects.particle import Particle
from src.database.objects.skin import Skin
from src.database.objects.user import User as UserObject
from src.models.sonolus_resource_locator import SonolusResourceLocator
from src.models.user_total_publish import UserTotalPublish


class MustHaveName(metaclass=ABCMeta):
    """名前を持つオブジェクトを表す基底クラス"""

    name: str


T = TypeVar("T", bound=MustHaveName)


class MustHaveUserId(metaclass=ABCMeta):
    """ユーザーIDを持つオブジェクトを表す基底クラス"""

    userId: str


U = TypeVar("U", bound=MustHaveUserId)


class MustHaveTime(metaclass=ABCMeta):
    """最低限時間は持っているオブジェクトを表す基底クラス"""

    userId: int
    createdTime: int
    updatedTime: int


V = TypeVar("V", bound=MustHaveTime)


class MustHaveVersionAndUserId(metaclass=ABCMeta):
    """最低限時間は持っているオブジェクトを表す基底クラス"""

    userId: int
    version: int


W = TypeVar("W", bound=MustHaveVersionAndUserId)


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


def copy_translate_fields(model: Any, field_names: List[str]) -> Any:
    """指定したフィールドそれぞれの英名フィールドが空なら日本語フィールドからコピーする"""
    for k in field_names:
        if not hasattr(model, k):
            continue
        attr_name = f"{k}En"
        if getattr(model, attr_name) is None:
            setattr(model, attr_name, getattr(model, k))
    return model


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


def patch_to_model(
    model: V,
    updates: Dict[str, Union[str, Dict[str, str]]],
    locator_names: List[str],
    extend_excludes: Optional[List[str]],
) -> V:
    """指定されたモデルに、与えられた辞書から要素を反映する"""
    excludes = [
        "id",
        "userId",
        "createdTime",
        "updatedTime",
    ]
    if extend_excludes:
        excludes += extend_excludes
    for k in excludes:
        updates.pop(k, None)
    for k, v in updates.items():
        if k not in locator_names:
            setattr(model, k, v)
        else:
            r: Dict[str, str] = v  # type: ignore
            if "hash" in r.keys():
                setattr(model, k, r["hash"])
    model.updatedTime = get_current_unix()
    return model


class DataBridge:
    """"リクエスト/DB/レスポンスの変換支援クラス"""

    def __init__(
        self,
        db: AsyncSession,
        auth: Optional[FirebaseClaims],
        object_name: str,
        locator_names: List[str],
        object_version: int,
        is_new: bool,
    ):
        self.db = db
        self.auth = auth
        self.object_name = object_name
        self.locator_names = locator_names
        self.version = object_version
        self.is_new = is_new

    async def to_db(self, model: V) -> None:
        """指定されたモデルのSRLフィールドをハッシュだけにし、調整してDBに格納可能にする"""
        if self.auth:
            model.userId = await get_internal_id(self.db, self.auth["user_id"])
        for k in self.locator_names:
            field = getattr(model, k)
            if field is None:
                raise HTTPException(
                    status_code=400, detail=f"Bad Request: {k} is missing"
                )
            setattr(model, k, field.hash)
        delattr(model, "version")
        copy_translate_fields(
            model, ["title", "description", "author", "subtitle", "artists"]
        )
        model.updatedTime = get_current_unix()
        if self.is_new:
            model.createdTime = model.updatedTime

    def to_resp(self, model: W) -> None:
        """指定されたモデルのSRLフィールドをSRLにし、調整して応答可能にする (引数は全て小文字)"""
        for k in self.locator_names:
            hash = getattr(model, k)
            resource_type = f"{self.object_name.capitalize()}{k.capitalize()}"
            srl = SonolusResourceLocator(
                type=resource_type,
                hash=hash,
                url=f"{CDN_ENDPOINT}/repository/{resource_type}/{hash}",
            )
            setattr(model, k, srl)
        model.version = self.version
        if self.auth:
            model.userId = self.auth["user_id"]
