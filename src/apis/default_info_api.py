# coding: utf-8

import asyncio

from fastapi import APIRouter
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import dependsDatabase
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
    db: AsyncSession = dependsDatabase,
) -> ServerInfo:
    """It returns small list of all infos registered in this server.
    (It should be trimmed if the server has too many items)"""
    stubPage: Page = Page(items=[], total=0, page=1, size=1)
    getSize: Params = Params(page=1, size=5)
    levels: Page[LevelObject] = stubPage
    skins: Page[SkinObject] = stubPage
    backgrounds: Page[BackgroundObject] = stubPage
    effects: Page[EffectObject] = stubPage
    particles: Page[ParticleObject] = stubPage
    engines: Page[EngineObject] = stubPage
    levels, skins, backgrounds, effects, particles, engines = await asyncio.gather(
        paginate(db, select(LevelObject), getSize),
        paginate(db, select(SkinObject), getSize),
        paginate(db, select(BackgroundObject), getSize),
        paginate(db, select(EffectObject), getSize),
        paginate(db, select(ParticleObject), getSize),
        paginate(db, select(EngineObject), getSize),
    )  # type: ignore
    return ServerInfo(
        levels=ServerInfoLevels(items=levels.items, search=levelSearch),
        skins=ServerInfoSkins(items=skins.items, search=defaultSearch),
        backgrounds=ServerInfoBackgrounds(
            items=backgrounds.items, search=defaultSearch
        ),
        effects=ServerInfoEffects(items=effects.items, search=defaultSearch),
        particles=ServerInfoParticles(items=particles.items, search=defaultSearch),
        engines=ServerInfoEngines(items=engines.items, search=defaultSearch),
    )
