import asyncio
from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, List, TypeVar

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import Column, Integer, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.constraints import (
    BACKGROUND_VERSION,
    EFFECT_VERSION,
    PARTICLE_VERSION,
    SKIN_VERSION,
)
from src.cruds.utils import DataBridge, get_first_item_or_404
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

from src.cruds.constraints import (  # LEVEL_LOCATORS,; ENGINE_LOCATORS,
    BACKGROUND_LOCATORS,
    EFFECT_LOCATORS,
    PARTICLE_LOCATORS,
    SKIN_LOCATORS,
)

PAGE_SIZE: Params = Params(page=1, size=5)


@dataclass
class BridgeObject:
    page: Page[Any]
    object_name: str
    locator_names: List[str]
    object_version: int


class MustBeDatabaseObj(metaclass=ABCMeta):
    updatedTime = Column(Integer)


T = TypeVar("T", bound=MustBeDatabaseObj)


async def get_content_page(db: AsyncSession, obj: T) -> Page[T]:
    """指定されたオブジェクトを更新が新しい順に5件取得します"""
    return paginate(
        db, select(obj).order_by(obj.updatedTime.desc()), PAGE_SIZE
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
    levels: List[LevelSave] = [a.toLevelItem() for a in announces]
    return levels


async def bulk_to_resp(
    db: AsyncSession, localization: str, bridge_objects: List[BridgeObject]
) -> None:
    """応答型に変換したいオブジェクト配列を渡すとそれぞれを応答型に変換します"""
    for obj in bridge_objects:
        bridge = DataBridge(db, obj.object_name, obj.locator_names, obj.object_version)
        for obj in obj.page.items:
            bridge.to_resp(obj, localization)


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
    levels: Page[LevelSave]
    skins: Page[SkinSave]
    backgrounds: Page[BackgroundSave]
    effects: Page[EffectSave]
    particles: Page[ParticleSave]
    engines: Page[EngineSave]
    objects = [
        LevelSave,
        SkinSave,
        BackgroundSave,
        EffectSave,
        ParticleSave,
        EngineSave,
    ]
    levels, skins, backgrounds, effects, particles, engines = await asyncio.gather(
        *[get_content_page(db, obj) for obj in objects]
    )
    bridge_objects: List[BridgeObject] = [
        # BridgeObject(levels, "level", PARTICLE_LOCATORS, PARTICLE_VERSION),
        BridgeObject(skins, "skin", SKIN_LOCATORS, SKIN_VERSION),
        BridgeObject(
            backgrounds, "background", BACKGROUND_LOCATORS, BACKGROUND_VERSION
        ),
        BridgeObject(effects, "effect", EFFECT_LOCATORS, EFFECT_VERSION),
        BridgeObject(particles, "particle", PARTICLE_LOCATORS, PARTICLE_VERSION),
        # BridgeObject(engines, "engine", ENGINE_LOCATORS, ENGINE_VERSION),
    ]
    bulk_to_resp(db, localization, bridge_objects)
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
