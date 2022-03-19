import asyncio
from typing import Tuple, TypeVar

from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import false, select, true
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.cruds.utils.db import get_first_item_or_404
from src.cruds.utils.info import AbstractInfoCrud
from src.cruds.utils.tile import create_tile
from src.database.mixins.sonolus_data import SonolusDataMixin
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.level import Level as LevelSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave
from src.database.objects.user import User as UserSave
from src.models.server_info import ServerInfo

T = TypeVar("T", bound=SonolusDataMixin)


class UserInfoCrud(AbstractInfoCrud):
    async def get_objects(
        self, db: AsyncSession
    ) -> Tuple[
        Page[SkinSave], Page[BackgroundSave], Page[EffectSave], Page[ParticleSave]
    ]:
        """譜面とエンジン以外をまとめて取得"""
        skins, backgrounds, effects, particles = await asyncio.gather(
            *[
                paginate(
                    db,
                    select(obj)
                    .filter(obj.isDeleted == false(), obj.public == true())
                    .order_by(obj.updatedTime.asc())
                    .options(
                        joinedload(obj.user),
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
        userId: str,
        localization: str,
    ) -> ServerInfo:
        """テストサーバーの情報を取得します"""
        user: UserSave = await get_first_item_or_404(
            db, select(UserSave).filter(UserSave.userId == userId)
        )
        tiles = [
            create_tile(
                "WELCOME_USERS",
                "ユーザーサーバー",
                "User server",
                user.userId,
                user.userId,
                user.userId,
                user.userId,
                user.description,
                user.description,
                1,
                "https://placehold.jp/150x150.png?text=ユーザーサーバー",
                "",
                localization,
            ),
        ]
        levels_filter_extends = [
            LevelSave.userId == user.id,
            LevelSave.public == true(),
        ]
        engines_filter_extends = [
            LevelSave.userId == user.id,
            LevelSave.public == true(),
        ]
        return await super().list_info(
            db,
            tiles,
            localization,
            False,
            levels_filter_extends,
            engines_filter_extends,
        )
