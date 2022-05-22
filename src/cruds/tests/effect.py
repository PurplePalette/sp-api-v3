from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from cruds.tests.tests_abstract import AbstractCrud
from src.database.objects.effect import Effect as EffectSave
from src.models.default_search import defaultSearch
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage


class TestsEffectCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """効果音セットを取得するクエリを返します"""
        return (
            select(EffectSave)
            .filter(
                EffectSave.name == name,
            )
            .options(joinedload(EffectSave.user))
        )

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetEffectResponse:
        """テスト中の効果音セットを取得します"""
        item = await super().get(db, name, localization)
        return GetEffectResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetEffectListResponse:
        """テスト中の効果音セット一覧を取得します"""
        sonolusPage: SonolusPage[EffectSave] = await super().list(
            db, EffectSave, testId, page, queries
        )
        return GetEffectListResponse(
            pageCount=sonolusPage.pageCount if sonolusPage.pageCount > 0 else 1,
            items=sonolusPage.items,
            search=defaultSearch,
        )
