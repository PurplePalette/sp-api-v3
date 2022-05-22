from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from cruds.tests.tests_abstract import AbstractCrud
from src.database.objects.skin import Skin as SkinSave
from src.models.default_search import defaultSearch
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage


class TestsSkinCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """スキンを取得するクエリを返します"""
        return (
            select(SkinSave)
            .filter(
                SkinSave.name == name,
            )
            .options(joinedload(SkinSave.user))
        )

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetSkinResponse:
        """テスト中のスキンを取得します"""
        item = await super().get(db, name, localization)
        return GetSkinResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetSkinListResponse:
        """テスト中のスキン一覧を取得します"""
        sonolusPage: SonolusPage[SkinSave] = await super().list(
            db, SkinSave, testId, page, queries
        )
        return GetSkinListResponse(
            pageCount=sonolusPage.pageCount if sonolusPage.pageCount > 0 else 1,
            items=sonolusPage.items,
            search=defaultSearch,
        )
