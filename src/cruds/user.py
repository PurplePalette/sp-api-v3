from datetime import datetime
from typing import List, Optional

import shortuuid
from fastapi import HTTPException  # noqa: F401
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select  # noqa: F401
from sqlalchemy.engine import Result  # noqa: F401
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils import (
    get_admin_or_403,
    get_current_unix,
    get_first_item_or_404,
    get_user_or_404,
    not_exist_or_409,
)
from src.database.objects.user import User as UserSave
from src.models.user import User as UserReqResp
from src.models.user_total import UserTotal
from src.models.user_total_publish import UserTotalPublish


async def create_user(
    db: AsyncSession, model: UserReqResp, user: FirebaseClaims
) -> UserReqResp:
    """ユーザーを追加します"""
    await not_exist_or_409(
        db,
        select(UserSave).filter(
            UserSave.userId == user["user_id"]
            or UserSave.accountId == model.accountId
            or UserSave.testId == model.testId
        ),
    )
    user_db = UserSave(**model.dict(exclude_unset=True))
    user_db.userId = user["user_id"]
    user_db.isAdmin = False
    user_db.isDeleted = False
    user_db.createdTime = user_db.updatedTime = get_current_unix()
    if user_db.accountId is None:
        user_db.accountId = shortuuid.uuid()
    if user_db.testId is None:
        user_db.testId = shortuuid.uuid()
    resp = UserReqResp.from_orm(user_db)
    resp.total = UserTotal(
        likes=0,
        plays=0,
        favorites=0,
        publish=UserTotalPublish(
            backgrounds=0, levels=0, particles=0, skins=0, effects=0, engines=0
        ),
    )
    db.add(user_db)
    await db.commit()
    await db.refresh(user_db)
    return resp


async def get_user(
    db: AsyncSession,
    name: str,
    user: Optional[FirebaseClaims],
) -> UserReqResp:
    """ユーザーを取得します"""
    user_db: UserSave = await get_first_item_or_404(
        db, select(UserSave).filter(UserSave.userId == name)
    )
    # 認証状態
    if user:
        # 同一IDではない場合非表示
        if user["user_id"] != user_db.userId:
            user_db.accountId = ""
            user_db.testId = ""
    # 認証状態でない場合非表示
    else:
        user_db.accountId = ""
        user_db.testId = ""
    resp = UserReqResp.from_orm(user_db)
    resp.total = UserTotal(
        likes=0,
        plays=0,
        favorites=0,
        publish=UserTotalPublish(
            backgrounds=0, levels=0, particles=0, skins=0, effects=0, engines=0
        ),
    )
    return resp


async def edit_user(
    db: AsyncSession,
    name: str,
    model: UserReqResp,
    user: FirebaseClaims,
) -> None:
    """ユーザーを編集します"""
    user_db: UserSave = await get_user_or_404(db, user)
    if user_db.displayId != name:
        await get_admin_or_403(db, user)
    model.updated_time = datetime.now()
    model.created_time = user_db.created_time()
    model.displayId = user_db.displayId
    model.is_admin = False
    model.is_deleted = False
    update_data = model.dict(exclude_unset=True)
    for k in update_data.keys():
        setattr(user_db, k, update_data[k])
    await db.commit()
    await db.refresh(user_db)


async def delete_user(
    db: AsyncSession,
    name: str,
    user: FirebaseClaims,
) -> None:
    """ユーザーを削除します"""
    user_db: UserSave = await get_first_item_or_404(
        db, select(UserSave).filter(UserSave.name == name)
    )
    if user_db.displayId != user.userId:
        await get_admin_or_403(db, user)
    user_db.is_deleted = True
    user_db.updated_time = datetime.now()
    db.add(user_db)
    await db.commit()
    await db.refresh(user_db)


async def list_user(
    db: AsyncSession,
) -> List[UserSave]:
    """ユーザー一覧を取得します"""
    resp: Result = await db.execute(
        select(UserSave).order_by(UserSave.updated_time.desc())
    )
    users: List[UserSave] = resp.scalars()
    users = [UserReqResp(**user.to_dict()) for user in users]
    return users
