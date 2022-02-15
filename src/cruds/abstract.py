from abc import ABCMeta, abstractmethod
from typing import Any

from fastapi_cloudauth.firebase import FirebaseClaims
from models.search_query import SearchQueries
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractCrud(metaclass=ABCMeta):
    """
    CRUD抽象クラス
    """

    @abstractmethod
    async def add(self, db: AsyncSession, model: Any, auth: FirebaseClaims) -> Any:
        pass

    @abstractmethod
    async def edit(
        self, db: AsyncSession, name: str, model: Any, auth: FirebaseClaims
    ) -> Any:
        pass

    @abstractmethod
    async def delete(self, db: AsyncSession, name: str, auth: FirebaseClaims) -> Any:
        return None

    @abstractmethod
    async def get(self, db: AsyncSession, name: str, localization: str) -> Any:
        pass

    @abstractmethod
    async def list(self, db: AsyncSession, page: int, queries: SearchQueries) -> Any:
        pass
