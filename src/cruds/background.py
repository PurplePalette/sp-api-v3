import asyncio
from typing import Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    db_to_resp,
    get_current_unix,
    get_first_item_or_404,
    get_new_name,
    is_owner_or_admin_otherwise_409,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.database.objects import BackgroundSave
from src.models.add_background_request import AddBackgroundRequest
from src.models.background import Background as BackgroundReqResp
from src.models.default_search import defaultSearch
from src.models.edit_background_request import EditBackgroundRequest
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage


async def create_background(
    db: AsyncSession, model: AddBackgroundRequest, auth: FirebaseClaims
) -> Union[HTTPException, GetBackgroundResponse]:
    """背景を追加します"""
    background_db = BackgroundSave(**model.dict())
    background_db.name = await get_new_name(db, BackgroundSave)
    background_db.userId = auth["user_id"]
    await req_to_db(db, background_db, is_new=True)
    await save_to_db(db, background_db)
    await db_to_resp(db, background_db)
    item = BackgroundReqResp.from_orm(background_db)
    resp = GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_background(
    db: AsyncSession, name: str, localization: str
) -> GetBackgroundResponse:
    """背景を取得します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db, select(BackgroundSave).filter(BackgroundSave.name == name)
    )
    await db_to_resp(db, background_db, localization)
    item = BackgroundReqResp.from_orm(background_db)
    return GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_background(
    db: AsyncSession,
    name: str,
    model: EditBackgroundRequest,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetBackgroundResponse]:
    """背景を編集します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db,
        select(BackgroundSave).filter(
            BackgroundSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, background_db, auth)
    patch_to_model(background_db, model.dict(exclude_unset=True))
    await save_to_db(db, background_db)
    await db_to_resp(db, background_db)
    item = BackgroundReqResp.from_orm(background_db)
    return GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_background(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """背景を削除します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db, select(BackgroundSave).filter(BackgroundSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, background_db, auth)
    background_db.isDeleted = True
    background_db.updatedTime = get_current_unix()
    await save_to_db(db, background_db)
    return None


async def list_background(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetBackgroundListResponse:
    """背景一覧を取得します"""
    select_query = buildDatabaseQuery(BackgroundSave, queries)
    userPage: Page[BackgroundSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    resp: SonolusPage = toSonolusPage(userPage)
    await asyncio.gather(*[db_to_resp(db, r, queries.localization) for r in resp.items])
    return GetBackgroundListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )
