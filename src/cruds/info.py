import asyncio
from abc import ABCMeta
from typing import Any, List, TypeVar

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import Column, Integer, false, select, true
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from src.cruds.utils import db_to_resp, get_first_item_or_404
from src.database.objects import (
    AnnounceSave,
    BackgroundSave,
    EffectSave,
    EngineSave,
    LevelSave,
    ParticleSave,
    SkinSave,
)
from src.models.background import Background as BackgroundResp
from src.models.default_search import defaultSearch, levelSearch
from src.models.effect import Effect as EffectResp
from src.models.engine import Engine as EngineResp
from src.models.level import Level as LevelResp
from src.models.particle import Particle as ParticleResp
from src.models.server_info import ServerInfo
from src.models.server_info_backgrounds import ServerInfoBackgrounds
from src.models.server_info_effects import ServerInfoEffects
from src.models.server_info_engines import ServerInfoEngines
from src.models.server_info_levels import ServerInfoLevels
from src.models.server_info_particles import ServerInfoParticles
from src.models.server_info_skins import ServerInfoSkins
from src.models.skin import Skin as SkinResp

PAGE_SIZE: Params = Params(page=1, size=5)


class MustBeDatabaseObj(metaclass=ABCMeta):
    updatedTime = Column(Integer)


T = TypeVar("T", bound=MustBeDatabaseObj)


async def get_content_page(db: AsyncSession, obj: T) -> Page[T]:
    """指定されたオブジェクトを更新が新しい順に5件取得します"""
    return await paginate(
        db,
        select(obj).order_by(obj.updatedTime.desc()),
        PAGE_SIZE,
    )  # type: ignore


async def get_announces(db: AsyncSession, announceIds: List[int]) -> List[LevelSave]:
    """指定されたID一覧のアナウンスを取得します"""
    announces = await asyncio.gather(
        *[
            get_first_item_or_404(
                db, select(AnnounceSave).filter(AnnounceSave.id == id)
            )
            for id in announceIds
        ]
    )
    await asyncio.gather(*[db_to_resp(db, announce) for announce in announces])
    levels: List[LevelSave] = [a.toItem() for a in announces]
    return levels


def create_server_info(
    levels: List[LevelResp],
    backgrounds: List[BackgroundResp],
    engines: List[EngineResp],
    effects: List[EffectResp],
    particles: List[ParticleResp],
    skins: List[SkinResp],
) -> ServerInfo:
    """与えられた各要素からサーバー情報の応答を作成します"""
    return ServerInfo(
        levels=ServerInfoLevels(
            items=levels,
            search=levelSearch,
        ),
        skins=ServerInfoSkins(items=skins, search=defaultSearch),
        backgrounds=ServerInfoBackgrounds(items=backgrounds, search=defaultSearch),
        effects=ServerInfoEffects(items=effects, search=defaultSearch),
        particles=ServerInfoParticles(items=particles, search=defaultSearch),
        engines=ServerInfoEngines(items=engines, search=defaultSearch),
    )


async def list_info(db: AsyncSession, localization: str) -> ServerInfo:
    """サーバー情報を取得します"""
    tiles: List[LevelSave] = await get_announces(db, [1, 2])
    # joinedload すべきだが、どうやらjoinedloadはlazyできるらしい
    levels: Page[LevelSave] = await paginate(
        db,
        select(LevelSave)
        .order_by(LevelSave.updatedTime.desc())
        .options(
            joinedload(LevelSave.genre),
            selectinload(LevelSave.likes),
            selectinload(LevelSave.favorites),
            joinedload(LevelSave.engine).options(
                joinedload(EngineSave.background),
                joinedload(EngineSave.skin),
                joinedload(EngineSave.effect),
                joinedload(EngineSave.particle),
            ),
        ),
        PAGE_SIZE,
    )  # type: ignore
    skins: Page[SkinSave]
    backgrounds: Page[BackgroundSave]
    effects: Page[EffectSave]
    particles: Page[ParticleSave]
    engines: Page[EngineSave]
    objects = [SkinSave, BackgroundSave, EffectSave, ParticleSave, EngineSave]
    # 各要素リストの生成
    skins, backgrounds, effects, particles, engines = await asyncio.gather(
        *[
            paginate(
                db,
                select(obj)
                .filter(obj.isDeleted == false(), obj.public == true())
                .order_by(obj.updatedTime.asc())
                .options(
                    selectinload(obj.user),
                ),
                PAGE_SIZE,
            )
            for obj in objects
        ]
    )  # type: ignore
    # 応答型に変換
    bridge_objects: List[Page[Any]] = [
        levels,
        skins,
        backgrounds,
        effects,
        particles,
        engines,
    ]
    for obj in bridge_objects:
        await asyncio.gather(
            *[db_to_resp(db, item, localization) for item in obj.items]
        )
        obj.items = [item.toItem() for item in obj.items]
    # お知らせとレベルを結合
    tile_and_levels: List[LevelResp] = tiles + list(
        (levels.items if len(levels.items) <= 3 else levels.items[:2])
    )
    return create_server_info(
        levels=tile_and_levels,
        backgrounds=list(backgrounds.items),
        engines=list(engines.items),
        effects=list(effects.items),
        particles=list(particles.items),
        skins=list(skins.items),
    )
