import asyncio
from typing import Any, List, Optional, Tuple, TypeVar

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import false, select, true
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from src.cruds.utils import db_to_resp
from src.database.mixins.sonolus_data import SonolusDataMixin
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.level import Level as LevelSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave
from src.models.background import Background as BackgroundResp
from src.models.default_search import (
    defaultSearch,
    defaultUserSearch,
    levelSearch,
    levelUserSearch,
)
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

T = TypeVar("T", bound=SonolusDataMixin)


class AbstractInfoCrud:
    PAGE_SIZE = Params(page=1, size=5)
    SIMPLE_OBJECTS = [SkinSave, BackgroundSave, EffectSave, ParticleSave]

    def get_levels_selector(self, extends_filter: Optional[List[Any]] = None) -> select:
        """譜面取得のセレクタ"""
        filters = [
            LevelSave.isDeleted == false(),
        ]
        if extends_filter:
            filters += extends_filter
        return select(LevelSave).filter(*filters)

    def get_engines_selector(
        self, extends_filter: Optional[List[Any]] = None
    ) -> select:
        """エンジン取得のセレクタ"""
        filters = [
            EngineSave.isDeleted == false(),
        ]
        if extends_filter:
            filters += extends_filter
        return select(EngineSave).filter(*filters)

    async def get_objects(
        self, db: AsyncSession
    ) -> Tuple[
        Page[SkinSave], Page[BackgroundSave], Page[EffectSave], Page[ParticleSave]
    ]:
        """譜面以外をまとめて取得"""
        skins, backgrounds, effects, particles = await asyncio.gather(
            *[
                paginate(
                    db,
                    select(obj)
                    .filter(obj.isDeleted == false(), obj.public == true())
                    .order_by(obj.updatedTime.asc())
                    .options(
                        selectinload(obj.user),
                    ),
                    self.PAGE_SIZE,
                )
                for obj in self.SIMPLE_OBJECTS
            ]
        )
        return skins, backgrounds, effects, particles

    async def list_info(
        self,
        db: AsyncSession,
        tiles: List[LevelSave],
        localization: str,
        use_user: bool,
        levels_filter_extends: Optional[List[Any]] = None,
        engines_filter_extends: Optional[List[Any]] = None,
    ) -> ServerInfo:
        """サーバー情報を取得します"""
        levels: Page[LevelSave] = await paginate(
            db,
            self.get_levels_selector(levels_filter_extends)
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
            self.PAGE_SIZE,
        )  # type: ignore
        engines: Page[EngineSave] = await paginate(
            db,
            self.get_engines_selector(engines_filter_extends)
            .order_by(LevelSave.updatedTime.desc())
            .options(
                joinedload(EngineSave.background).options(
                    joinedload(BackgroundSave.user),
                ),
                joinedload(EngineSave.skin).options(
                    joinedload(SkinSave.user),
                ),
                joinedload(EngineSave.particle).options(
                    joinedload(ParticleSave.user),
                ),
                joinedload(EngineSave.effect).options(
                    joinedload(EffectSave.user),
                ),
                joinedload(EngineSave.user),
            ),
            self.PAGE_SIZE,
        )  # type: ignore
        skins: Page[SkinSave]
        backgrounds: Page[BackgroundSave]
        effects: Page[EffectSave]
        particles: Page[ParticleSave]
        # 各要素リストの生成
        skins, backgrounds, effects, particles = await self.get_objects(db)
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
            use_user=use_user,
        )


def create_server_info(
    levels: List[LevelResp],
    backgrounds: List[BackgroundResp],
    engines: List[EngineResp],
    effects: List[EffectResp],
    particles: List[ParticleResp],
    skins: List[SkinResp],
    use_user: bool,
) -> ServerInfo:
    return ServerInfo(
        levels=ServerInfoLevels(
            items=levels,
            search=levelSearch if not use_user else levelUserSearch,
        ),
        skins=ServerInfoSkins(
            items=skins, search=defaultSearch if not use_user else defaultUserSearch
        ),
        backgrounds=ServerInfoBackgrounds(
            items=backgrounds,
            search=defaultSearch if not use_user else defaultUserSearch,
        ),
        effects=ServerInfoEffects(
            items=effects, search=defaultSearch if not use_user else defaultUserSearch
        ),
        particles=ServerInfoParticles(
            items=particles, search=defaultSearch if not use_user else defaultUserSearch
        ),
        engines=ServerInfoEngines(
            items=engines, search=defaultSearch if not use_user else defaultUserSearch
        ),
    )
