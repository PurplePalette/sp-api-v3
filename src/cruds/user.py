from datetime import datetime
from typing import List, Optional  # noqa: F401

from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy import select  # noqa: F401
from sqlalchemy.engine import Result  # noqa: F401
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils import get_first_item_or_404  # noqa: F401
from src.cruds.utils import not_exist_or_409  # noqa: F401
from src.cruds.utils import get_admin_or_403, get_user_or_404
from src.database.objects.user import User as UserSave
from src.models.user import User as UserReqResp


async def create_user(
    db: AsyncSession, model: UserReqResp, user: FirebaseClaims
) -> UserReqResp:
    """ユーザーを追加します"""
    await not_exist_or_409(db, select(UserSave).filter(UserSave.name == user.user_id))
    user_db: UserSave = UserSave(
        name=user.user_id,
        display_id=model.display_id,
        test_id=model.test_id,
        account_id=model.account_id,
        is_admin=False,
        is_deleted=False,
        created_time=datetime.now(),
        updated_time=datetime.now(),
    )
    user_resp: UserReqResp = UserReqResp(**user_db.to_dict())
    await db.commit()
    await db.refresh(user_db)
    return user_resp


async def get_user(
    db: AsyncSession,
    name: str,
    user: Optional[FirebaseClaims],
) -> UserReqResp:
    """ユーザーを取得します"""
    user_db: UserSave = await get_first_item_or_404(
        db, select(UserSave).filter(UserSave.name == name)
    )
    # 認証状態
    if user:
        # 同一IDではない場合非表示
        if user.user_id != user_db.display_id:
            user_db.account_id = ""
            user_db.test_id = ""
    # 認証状態でない場合非表示
    else:
        user_db.account_id = ""
        user_db.test_id = ""
    user_resp: UserReqResp = UserReqResp(**user_db.to_dict())
    return user_resp


async def edit_user(
    db: AsyncSession,
    name: str,
    model: UserReqResp,
    user: FirebaseClaims,
) -> None:
    """ユーザーを編集します"""
    user_db: UserSave = await get_user_or_404(db, user)
    if user_db.display_id != name:
        await get_admin_or_403(db, user)
    model.updated_time = datetime.now()
    model.created_time = user_db.created_time()
    model.display_id = user_db.display_id
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
    if user_db.display_id != user.user_id:
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
