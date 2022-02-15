# coding: utf-8

import asyncio
from dataclasses import dataclass
from typing import Any, List

from fastapi import APIRouter
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import dependsDatabase, dependsLocalization

# from src.cruds.skin import LOCATOR_NAMES as PARTICLE_LOCATORS
from src.cruds.constraints import (
    BACKGROUND_LOCATORS,
    BACKGROUND_VERSION,
    EFFECT_LOCATORS,
    EFFECT_VERSION,
    PARTICLE_LOCATORS,
    PARTICLE_VERSION,
    SKIN_LOCATORS,
    SKIN_VERSION,
)
from src.cruds.utils import DataBridge, get_first_item_or_404
from src.database.objects.announce import Announce as AnnounceObject
from src.database.objects.background import Background as BackgroundObject
from src.database.objects.effect import Effect as EffectObject
from src.database.objects.engine import Engine as EngineObject
from src.database.objects.level import Level as LevelObject
from src.database.objects.particle import Particle as ParticleObject
from src.database.objects.skin import Skin as SkinObject
from src.models.default_search import defaultSearch, levelSearch
from src.models.server_info import ServerInfo
from src.models.server_info_backgrounds import ServerInfoBackgrounds
from src.models.server_info_effects import ServerInfoEffects
from src.models.server_info_engines import ServerInfoEngines
from src.models.server_info_levels import ServerInfoLevels
from src.models.server_info_particles import ServerInfoParticles
from src.models.server_info_skins import ServerInfoSkins

router = APIRouter()


@dataclass
class BridgeObject:
    page: Page[Any]
    object_name: str
    locator_names: List[str]
    object_version: int


@router.get(
    "/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["default_info"],
    summary="Get default server info",
    response_model=ServerInfo,
)
async def get_server_info(
    db: AsyncSession = dependsDatabase, localization: str = dependsLocalization
) -> ServerInfo:
    """It returns small list of all infos registered in this server.
    (It should be trimmed if the server has too many items)"""
    tile1: AnnounceObject
    tile2: AnnounceObject
    tile1, tile2 = await asyncio.gather(
        get_first_item_or_404(
            db, select(AnnounceObject).filter(AnnounceObject.id == 1)
        ),
        get_first_item_or_404(
            db, select(AnnounceObject).filter(AnnounceObject.id == 2)
        ),
    )
    tiles: List[LevelObject] = [t.toLevelItem() for t in [tile1, tile2]]
    getSize: Params = Params(page=1, size=5)
    levels: Page[LevelObject]
    skins: Page[SkinObject]
    backgrounds: Page[BackgroundObject]
    effects: Page[EffectObject]
    particles: Page[ParticleObject]
    engines: Page[EngineObject]
    levels, skins, backgrounds, effects, particles, engines = await asyncio.gather(
        *[
            paginate(db, select(obj).order_by(obj.updatedTime.desc()), getSize)
            for obj in [
                LevelObject,
                SkinObject,
                BackgroundObject,
                EffectObject,
                ParticleObject,
                EngineObject,
            ]
        ]
    )
    bridge_objects: List[BridgeObject] = [
        BridgeObject(particles, "particle", PARTICLE_LOCATORS, PARTICLE_VERSION),
        BridgeObject(
            backgrounds, "background", BACKGROUND_LOCATORS, BACKGROUND_VERSION
        ),
        BridgeObject(effects, "effect", EFFECT_LOCATORS, EFFECT_VERSION),
        BridgeObject(skins, "skin", SKIN_LOCATORS, SKIN_VERSION),
    ]
    for obj in bridge_objects:
        bridge = DataBridge(db, obj.object_name, obj.locator_names, obj.object_version)
        for obj in obj.page.items:
            bridge.to_resp(obj, localization)
    return ServerInfo(
        levels=ServerInfoLevels(
            items=tiles
            + list((levels.items if len(levels.items) <= 3 else levels.items[:2])),
            search=levelSearch,
        ),
        skins=ServerInfoSkins(items=skins.items, search=defaultSearch),
        backgrounds=ServerInfoBackgrounds(
            items=backgrounds.items, search=defaultSearch
        ),
        effects=ServerInfoEffects(items=effects.items, search=defaultSearch),
        particles=ServerInfoParticles(items=particles.items, search=defaultSearch),
        engines=ServerInfoEngines(items=engines.items, search=defaultSearch),
    )
