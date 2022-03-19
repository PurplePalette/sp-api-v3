import asyncio

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.cruds.tests.abstract import AbstractCrud
from src.cruds.utils.db import get_first_item_or_404
from src.cruds.utils.models import db_to_resp
from src.cruds.utils.search import buildDatabaseQuery
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave
from src.database.objects.user import User as UserSave
from src.models.default_search import defaultSearch
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.search_query import SearchQueries, SearchStatus
from src.models.sonolus_page import SonolusPage, toSonolusPage


class UsersEngineCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """エンジンを取得するクエリを返します"""
        return (
            select(EngineSave)
            .filter(
                EngineSave.name == name,
            )
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
            )
        )

    async def bulk_db_to_resp(
        self, db: AsyncSession, engine_db: EngineSave, localization: str = "ja"
    ) -> None:
        # 各地のSRLを応答型に変換し回る
        for db_obj in [
            engine_db,
            engine_db.skin,
            engine_db.background,
            engine_db.particle,
            engine_db.effect,
        ]:
            await db_to_resp(db, db_obj, localization)

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetEngineResponse:
        """テスト中のエンジンを取得します"""
        engine_db: EngineSave = await get_first_item_or_404(
            db,
            self.get_query(name),
        )
        await self.bulk_db_to_resp(db, engine_db, localization)
        item = engine_db.toItem()
        return GetEngineResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetEngineListResponse:
        """テスト中のエンジン一覧を取得します"""
        user: UserSave = await get_first_item_or_404(
            db, select(UserSave).filter(UserSave.testId == testId)
        )
        queries.user = user
        queries.status = SearchStatus.TESTING
        select_query = buildDatabaseQuery(EngineSave, queries, False)
        respPage: Page[EngineSave] = await paginate(
            db,
            select_query.options(
                joinedload(EngineSave.user),
                joinedload(EngineSave.background).options(
                    joinedload(BackgroundSave.user)
                ),
                joinedload(EngineSave.skin).options(joinedload(SkinSave.user)),
                joinedload(EngineSave.particle).options(joinedload(ParticleSave.user)),
                joinedload(EngineSave.effect).options(joinedload(EffectSave.user)),
            ),
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage[EngineSave] = toSonolusPage(respPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        resp.items = [r.toItem() for r in resp.items]
        return GetEngineListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
