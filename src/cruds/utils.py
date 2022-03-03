import asyncio
import time
from abc import ABCMeta
from typing import Any, Dict, List, Optional, TypeVar, Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from shortuuid import ShortUUID
from sqlalchemy import func, select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true
from src.config import CDN_ENDPOINT
from src.cruds.constraints import SRL_BRIDGES, SRLDefine
from src.database.objects import UploadSave
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

    userId: Union[int, str]
    createdTime: int
    updatedTime: int


V = TypeVar("V", bound=MustHaveTime)


class MustHaveVersionAndUserId(metaclass=ABCMeta):
    """ユーザーIDとバージョンは持っているオブジェクトを表す基底クラス"""

    userId: Union[int, str]
    version: int


W = TypeVar("W", bound=MustHaveVersionAndUserId)


def get_current_unix() -> int:
    """現在のUNIX時刻を取得"""
    return int(time.time())


def get_random_name() -> str:
    """ランダムな12文字のnameを取得"""
    random_name: str = ShortUUID(
        alphabet="1234567890abcdefghijklmnopqrstuvwxyz"
    ).random(length=12)
    return random_name


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
    user = await db.execute(select(UserObject.id).filter(UserObject.userId == userId))
    res: Optional[int] = user.scalars().first()
    if res is None:
        raise HTTPException(
            status_code=401, detail="Your account is not registered in this server"
        )
    return res


async def get_display_id(db: AsyncSession, id: int) -> str:
    """指定された内部ID(データベースID)のユーザーの表示ID(FirebaseID)を取得"""
    user = await db.execute(select(UserObject.userId).filter(UserObject.id == id))
    res: Optional[str] = user.scalars().first()
    if res is None:
        raise Exception("Your account is not registered in this server")
    return res


def all_fields_exists_or_400(fields: List[Optional[Any]]) -> Optional[HTTPException]:
    """指定した全てのフィールドが存在しなければBadRequest"""
    for field in fields:
        if field is None:
            return HTTPException(
                status_code=400, detail="Bad request: missing required field"
            )
    return None


def copy_translate_fields(model: Any, field_names: List[str]) -> Any:
    """指定したフィールドそれぞれの英名フィールドが空なら日本語フィールドからコピーする"""
    for k in field_names:
        if not hasattr(model, k):
            continue
        attr_name = f"{k}En"
        if getattr(model, attr_name) is None:
            setattr(model, attr_name, getattr(model, k))
    return model


def move_translate_fields(model: Any, field_names: List[str]) -> Any:
    """指定したフィールドそれぞれの英名フィールドで日本語フィールドを上書きする"""
    for k in field_names:
        if not hasattr(model, k):
            continue
        attr_name = f"{k}En"
        if getattr(model, attr_name) is not None:
            setattr(model, k, getattr(model, attr_name))
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
    extend_excludes: Optional[List[str]] = None,
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
        setattr(model, k, v)
    model.updatedTime = get_current_unix()
    return model


async def req_to_db(
    db: AsyncSession, model: V, is_new: bool = False
) -> Optional[HTTPException]:
    """リクエストモデルをデータベースモデルにするショートハンド"""
    # Firebase側のIDをDB側のIDに変換
    model.userId = await get_internal_id(db, str(model.userId))
    # 英語の欠落フィールドを埋める
    copy_translate_fields(
        model, ["title", "description", "author", "subtitle", "artists"]
    )
    # データ更新時刻を埋める
    model.updatedTime = get_current_unix()
    if is_new:
        model.createdTime = model.updatedTime
    # 予め定義した SRL辞書から ロケータを取ってくる
    obj_name = type(model).__name__.lower()
    if not hasattr(SRL_BRIDGES, obj_name):
        raise Exception("No bridge for model: " + obj_name)
    bridge: SRLDefine = getattr(SRL_BRIDGES, obj_name)
    for k in bridge.locators:
        hash: str = getattr(model, k)
        obj_exist = await is_exist(db, select(UploadSave.objectHash == hash))
        if not obj_exist:
            return HTTPException(
                status_code=400,
                detail=f"Bad Request: SRL {obj_name} target {hash} was not found",
            )
    return None


async def db_to_resp(db: AsyncSession, model: W, localization: str = "ja") -> None:
    """データベースモデルをレスポンスモデルにするショートハンド"""
    # DB側のIDをFirebase側のIDに変換
    model.userId = await get_display_id(db, int(model.userId))
    # 予め定義した SRL辞書から バージョンとロケータを取ってくる
    obj_name = type(model).__name__.lower()
    if not hasattr(SRL_BRIDGES, obj_name):
        raise Exception("No bridge for model: " + obj_name)
    bridge: SRLDefine = getattr(SRL_BRIDGES, obj_name)
    model.version = bridge.obj_version
    for k in bridge.locators:
        hash = getattr(model, k)
        resource_type = f"{obj_name.capitalize()}{k.capitalize()}"
        srl = SonolusResourceLocator(
            type=resource_type,
            hash=hash,
            url=f"{CDN_ENDPOINT}/repository/{resource_type}/{hash}",
        )
        setattr(model, k, srl)
    # リクエスト言語が日本語でなければ英語で返す
    if localization != "ja":
        move_translate_fields(
            model, ["title", "description", "author", "subtitle", "artists"]
        )
