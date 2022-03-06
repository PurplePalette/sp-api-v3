import asyncio
from typing import Optional, Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import false, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.abstract import AbstractCrud
from src.cruds.utils import (
    get_current_unix,
    get_first_item_or_404,
    get_internal_id,
    get_random_name,
    get_user_or_404,
    is_owner_or_admin_otherwise_409,
    not_exist_or_409,
    patch_to_model,
    save_to_db,
)
from src.cruds.utils.totals import get_total_publish
from src.database.objects.user import User as UserSave
from src.models.add_user_request import AddUserRequest
from src.models.edit_user_request import EditUserRequest
from src.models.get_user_list_response import GetUserListResponse
from src.models.sonolus_page import SonolusPage, toSonolusPage
from src.models.user import User as UserReqResp
from src.models.user_total import UserTotal
from src.models.user_total_publish import UserTotalPublish


class UserCrud(AbstractCrud):  # type: ignore
    def get_query(self, name: str) -> select:
        """ユーザーを取得するクエリを返します"""
        return select(UserSave).filter(
            UserSave.userId == name,
        )

    async def get_named_item_or_404(self, db: AsyncSession, name: str) -> UserSave:
        """指定した名称のユーザーが存在すれば取得し、無ければ404を返します"""
        return await get_first_item_or_404(db, self.get_query(name))

    async def add(self, db: AsyncSession, model: AddUserRequest) -> UserReqResp:
        """ユーザーを追加します"""
        await not_exist_or_409(
            db,
            select(UserSave).filter(UserSave.userId == model.userId),
        )
        unixTime = get_current_unix()
        user_db = UserSave(
            userId=model.userId,
            isAdmin=False,
            isDeleted=False,
            createdTime=unixTime,
            updatedTime=unixTime,
            accountId=get_random_name(),
            testId=get_random_name(),
        )
        await save_to_db(db, user_db)
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

    async def get(
        self,
        db: AsyncSession,
        name: str,
        # 認証してるかどうかは任意
        user: Optional[FirebaseClaims],
    ) -> UserReqResp:
        """ユーザーを取得します"""
        user_db = await self.get_named_item_or_404(db, name)
        # 認証状態でなければ非表示
        if user is None:
            user_db.accountId = ""
            user_db.testId = ""
        # 同一IDではない場合非表示
        elif user_db.userId != user["user_id"]:
            user_db.accountId = ""
            user_db.testId = ""
        resp = UserReqResp.from_orm(user_db)
        publish = await get_total_publish(db, user_db.id)
        resp.total = UserTotal(
            likes=0,
            plays=0,
            favorites=0,
            publish=publish,
        )
        return resp

    async def edit(
        self,
        db: AsyncSession,
        model: EditUserRequest,
        user: FirebaseClaims,
    ) -> Union[HTTPException, UserReqResp]:
        """ユーザーを編集します"""
        user_db: UserSave = await get_user_or_404(db, user)
        await is_owner_or_admin_otherwise_409(db, user_db, user)
        patch_to_model(
            user_db,
            model.dict(exclude_unset=True),
            [
                "total",
                "isDeleted",
                "isAdmin",
            ],
        )
        await save_to_db(db, user_db)
        return UserReqResp.from_orm(user_db)

    async def delete(
        self,
        db: AsyncSession,
        name: str,
        user: FirebaseClaims,
    ) -> None:
        """ユーザーを削除します"""
        await super().delete(db, name, user)
        return None

    async def list(self, db: AsyncSession, page: int) -> GetUserListResponse:
        """ユーザー一覧を取得します"""
        userPage: Page[UserSave] = await paginate(
            db,
            select(UserSave)
            .filter(UserSave.isDeleted == false())
            .order_by(UserSave.updatedTime.desc()),
            Params(page=page + 1, size=20),
        )  # type: ignore
        for u in userPage.items:
            u.testId = "hidden"
            u.accountId = "hidden"
        userPage.items = [UserReqResp.from_orm(u) for u in userPage.items]
        await asyncio.gather(*[get_user_deep(db, u) for u in userPage.items])
        resp: SonolusPage = toSonolusPage(userPage)
        return GetUserListResponse(
            users=resp.items,
            total=resp.total,
            pages=resp.pageCount,
        )


async def get_user_deep(db: AsyncSession, user: UserSave) -> None:
    """投稿回数等深い部分まで取得する"""
    internal_id = await get_internal_id(db, user.userId)
    publish: UserTotalPublish = await get_total_publish(db, internal_id)
    user.total = UserTotal(
        likes=0,
        favorites=0,
        plays=0,
        publish=publish,
    )
