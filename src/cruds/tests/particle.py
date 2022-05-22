from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from cruds.tests.tests_abstract import AbstractCrud
from src.database.objects.particle import Particle as ParticleSave
from src.models.default_search import defaultSearch
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage


class TestsParticleCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """パーティクルを取得するクエリを返します"""
        return (
            select(ParticleSave)
            .filter(
                ParticleSave.name == name,
            )
            .options(joinedload(ParticleSave.user))
        )

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetParticleResponse:
        """テスト中のパーティクルを取得します"""
        item = await super().get(db, name, localization)
        return GetParticleResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetParticleListResponse:
        """テスト中のパーティクル一覧を取得します"""
        sonolusPage: SonolusPage[ParticleSave] = await super().list(
            db, ParticleSave, testId, page, queries
        )
        return GetParticleListResponse(
            pageCount=sonolusPage.pageCount if sonolusPage.pageCount > 0 else 1,
            items=sonolusPage.items,
            search=defaultSearch,
        )
