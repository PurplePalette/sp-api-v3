from abc import ABCMeta
from typing import Any, Dict, List, Optional, TypeVar, Union

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import CDN_ENDPOINT
from src.cruds.constraints import SRL_BRIDGES, SRLDefine
from src.cruds.utils.db import is_exist
from src.cruds.utils.funcs import get_current_unix
from src.cruds.utils.ids import get_display_id, get_internal_id
from src.database.objects import UploadSave
from src.models.sonolus_resource_locator import SonolusResourceLocator


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


def set_srl(model: W, obj_name: str) -> None:
    """指定されたオブジェクトのSRLフィールドをSRLインスタンスに変換する"""
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


async def db_to_resp(db: AsyncSession, model: W, localization: str = "ja") -> None:
    """データベースモデルをレスポンスモデルにするショートハンド"""
    # DB側のIDをFirebase側のIDに変換
    if type(model.userId) == int:
        model.userId = await get_display_id(db, int(model.userId))
    # 予め定義した SRL辞書から バージョンとロケータを取ってくる
    obj_name = type(model).__name__.lower()
    if not hasattr(SRL_BRIDGES, obj_name):
        raise Exception("No bridge for model: " + obj_name)
    set_srl(model, obj_name)
    # リクエスト言語が日本語でなければ英語で返す
    if localization != "ja":
        move_translate_fields(
            model, ["title", "description", "author", "subtitle", "artists"]
        )
