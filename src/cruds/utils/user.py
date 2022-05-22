from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from sqlalchemy import select, true
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils.db import (
    MustHaveUserId,
    get_first_item_or_403,
    get_first_item_or_404,
)
from src.security_api import FirebaseClaims

if TYPE_CHECKING:
    from src.database.objects.user import User as UserObject


async def get_user_or_404(
    db: AsyncSession,
    user: FirebaseClaims,
) -> UserObject:
    """データベースに指定されたユーザーが存在すれば取得、なければ NotFound"""
    from src.database.objects.user import User as UserObject

    user_db: UserObject = await get_first_item_or_404(
        db, select(UserObject).filter(UserObject.userId == user["user_id"])
    )
    return user_db


async def get_admin_or_403(
    db: AsyncSession,
    user: FirebaseClaims,
) -> UserObject:
    """データベースに指定された管理者ユーザーが存在すれば取得、なければ Forbidden"""
    from src.database.objects.user import User as UserObject

    user_db: UserObject = await get_first_item_or_403(
        db,
        select(UserObject).filter(
            UserObject.userId == user["user_id"], UserObject.isAdmin == true()
        ),
    )
    return user_db


U = TypeVar("U", bound=MustHaveUserId)


async def is_owner_or_admin_otherwise_409(
    db: AsyncSession, model: U, auth: FirebaseClaims
) -> None:
    """認証ユーザーが本人または管理者でなければ Forbidden"""
    if model.userId != auth["user_id"]:
        await get_admin_or_403(db, auth)
