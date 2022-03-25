from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.cruds.users.abstract import AbstractCrud
from src.database.objects.background import Background as BackgroundSave
from src.models.default_search import defaultSearch
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage


class UsersBackgroundCrud(AbstractCrud):
    def get_query(self, name: str) -> select:
        """背景を取得するクエリを返します"""
        return (
            select(BackgroundSave)
            .filter(
                BackgroundSave.name == name,
            )
            .options(joinedload(BackgroundSave.user))
        )

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetBackgroundResponse:
        """テスト中の背景を取得します"""
        item = await super().get(db, name, localization)
        return GetBackgroundResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def list(
        self, db: AsyncSession, testId: str, page: int, queries: SearchQueries
    ) -> GetBackgroundListResponse:
        """テスト中の背景一覧を取得します"""
        sonolusPage: SonolusPage[BackgroundSave] = await super().list(
            db, BackgroundSave, testId, page, queries
        )
        return GetBackgroundListResponse(
            pageCount=sonolusPage.pageCount if sonolusPage.pageCount > 0 else 1,
            items=sonolusPage.items,
            search=defaultSearch,
        )
