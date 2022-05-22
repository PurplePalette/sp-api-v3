from abc import ABCMeta, abstractmethod
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils.user import is_owner_or_admin_otherwise_409
from src.cruds.utils.db import (
    get_first_item_or_404,
    save_to_db,
)
from src.cruds.utils.funcs import get_current_unix
from src.models.search_query import SearchQueries
from src.security_api import FirebaseClaims


class AbstractCrud(metaclass=ABCMeta):
    """
    CRUD抽象クラス
    """

    @abstractmethod
    def get_query(self, name: str) -> select:
        """取得に必要なクエリを返します"""
        pass

    @abstractmethod
    async def get_named_item_or_404(self, db: AsyncSession, name: str) -> Any:
        """指定した名称の要素が存在すれば取得し、無ければ404を返します"""
        return await get_first_item_or_404(db, self.get_query(name))

    @abstractmethod
    async def add(self, db: AsyncSession, model: Any, auth: FirebaseClaims) -> Any:
        """要素を追加します"""
        pass

    @abstractmethod
    async def edit(
        self, db: AsyncSession, name: str, model: Any, auth: FirebaseClaims
    ) -> Any:
        """要素を編集します"""
        pass

    async def delete(
        self,
        db: AsyncSession,
        name: str,
        auth: FirebaseClaims,
    ) -> None:
        """要素を削除します"""
        item_db = await get_first_item_or_404(db, self.get_query(name))
        await is_owner_or_admin_otherwise_409(db, item_db, auth)
        item_db.isDeleted = True
        item_db.updatedTime = get_current_unix()
        await save_to_db(db, item_db)
        return None

    @abstractmethod
    async def get(self, db: AsyncSession, name: str, localization: str) -> Any:
        """要素を取得します"""
        pass

    @abstractmethod
    async def list(self, db: AsyncSession, page: int, queries: SearchQueries) -> Any:
        """要素一覧を取得します"""
        pass
