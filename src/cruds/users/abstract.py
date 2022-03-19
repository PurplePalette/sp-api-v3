import asyncio
from abc import ABCMeta, abstractmethod
from typing import Any, Optional, TypeVar

from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils.db import get_first_item_or_404
from src.cruds.utils.models import db_to_resp
from src.cruds.utils.search import buildDatabaseQuery
from src.database.mixins.sonolus_data import SonolusDataMixin
from src.database.objects.user import User as UserSave
from src.models.search_query import SearchQueries, SearchStatus
from src.models.sonolus_page import SonolusPage, toSonolusPage

T = TypeVar("T", bound=SonolusDataMixin)


class AbstractCrud(metaclass=ABCMeta):
    """
    テスト中のデータのCRUD抽象クラス
    """

    @abstractmethod
    def get_query(self, name: str) -> select:
        """取得に必要なクエリを返します"""
        pass

    async def get_named_item_or_404(self, db: AsyncSession, name: str) -> Any:
        return await get_first_item_or_404(db, self.get_query(name))

    async def get(self, db: AsyncSession, name: str, localization: str) -> Any:
        item_db = await self.get_named_item_or_404(db, name)
        await db_to_resp(db, item_db, localization)
        item = item_db.toItem()
        return item

    async def list(
        self,
        db: AsyncSession,
        obj: T,
        userId: str,
        page: int,
        queries: SearchQueries,  # 認証してるかどうかは任意
        authUser: Optional[FirebaseClaims],
    ) -> SonolusPage:
        user: UserSave = await get_first_item_or_404(
            db, select(UserSave).filter(UserSave.userId == userId)
        )
        queries.user = user
        if userId == authUser["user_id"]:
            queries.status = SearchStatus.all
        select_query = buildDatabaseQuery(obj, queries, True)
        respPage: Page[T] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage[T] = toSonolusPage(respPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        resp.items = [r.toItem() for r in resp.items]
        return resp
