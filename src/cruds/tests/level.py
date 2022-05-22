import asyncio

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from cruds.tests.tests_abstract import AbstractCrud
from src.cruds.utils.db import get_first_item_or_404
from src.cruds.utils.models import db_to_resp
from src.cruds.utils.search import buildDatabaseQuery
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.level import Level as LevelSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave
from src.database.objects.user import User as UserSave
from src.models import levelSearch
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.search_query import SearchQueries, SearchStatus
from src.models.sonolus_page import SonolusPage, toSonolusPage


class TestsLevelCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """レベルを取得するクエリを返します"""
        return (
            select(LevelSave)
            .filter(
                LevelSave.name == name,
            )
            .options(
                joinedload(LevelSave.genre),
                joinedload(LevelSave.user),
                selectinload(LevelSave.likes),
                selectinload(LevelSave.favorites),
                joinedload(LevelSave.engine).options(
                    joinedload(EngineSave.background).options(
                        joinedload(BackgroundSave.user)
                    ),
                    joinedload(EngineSave.skin).options(joinedload(SkinSave.user)),
                    joinedload(EngineSave.effect).options(joinedload(EffectSave.user)),
                    joinedload(EngineSave.particle).options(
                        joinedload(ParticleSave.user)
                    ),
                    joinedload(EngineSave.user),
                ),
            )
        )

    async def bulk_db_to_resp(
        self, db: AsyncSession, level_db: LevelSave, localization: str = "ja"
    ) -> None:
        # 各地のSRLを応答型に変換し回る
        for db_obj in [
            level_db,
            level_db.engine,
            level_db.engine.skin,
            level_db.engine.background,
            level_db.engine.particle,
            level_db.engine.effect,
        ]:
            await db_to_resp(db, db_obj, localization)

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetLevelResponse:
        """テスト中のレベルを取得します"""
        level_db: LevelSave = await get_first_item_or_404(
            db,
            self.get_query(name),
        )
        await self.bulk_db_to_resp(db, level_db, localization)
        item = level_db.toItem()
        return GetLevelResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetLevelListResponse:
        """テスト中のレベル一覧を取得します"""
        user: UserSave = await get_first_item_or_404(
            db, select(UserSave).filter(UserSave.testId == testId)
        )
        queries.user = user
        queries.status = SearchStatus.TESTING
        select_query = buildDatabaseQuery(LevelSave, queries, False)
        respPage: Page[LevelSave] = await paginate(
            db,
            select_query.options(
                joinedload(LevelSave.engine).options(
                    joinedload(EngineSave.user),
                    joinedload(EngineSave.background).options(
                        joinedload(BackgroundSave.user)
                    ),
                    joinedload(EngineSave.skin).options(joinedload(SkinSave.user)),
                    joinedload(EngineSave.particle).options(
                        joinedload(ParticleSave.user)
                    ),
                    joinedload(EngineSave.effect).options(joinedload(EffectSave.user)),
                ),
                joinedload(LevelSave.genre),
                joinedload(LevelSave.user),
                selectinload(LevelSave.likes),
                selectinload(LevelSave.favorites),
            ),
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage[LevelSave] = toSonolusPage(respPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        resp.items = [r.toItem() for r in resp.items]
        return GetLevelListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=levelSearch,
        )
