from typing import Union
import sqlalchemy  # noqa: F401
from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.search import buildDatabaseQuery
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.cruds.utils import (
    get_current_unix,
    get_first_item_or_404,
    is_owner_or_admin_otherwise_409,
    not_exist_or_409,
)
from src.database.objects.background import Background as BackgroundSave
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.sonolus_page import SonolusPage, toSonolusPage
from src.models.background import Background as BackgroundReqResp


async def create_background(
    db: AsyncSession, model: BackgroundReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetBackgroundResponse]:
    """背景を追加します"""
    await not_exist_or_409(
        db,
        select(BackgroundSave).filter(
            BackgroundSave.name == model.name,
        ),
    )
    background_db = BackgroundSave.from_orm(BackgroundReqResp)
    background_db.userId = auth["user_id"]
    background_db.createdTime = background_db.updatedTime = get_current_unix()
    background_db.thumbnail = model.thumbnail.hash
    background_db.data = model.data.hash
    background_db.image = model.image.hash
    background_db.configuration = model.configuration.hash
    item = BackgroundReqResp.from_orm(background_db)
    resp = GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    db.add(background_db)
    try:
        await db.commit()
        await db.refresh(background_db)
    except sqlalchemy.exc.IntegrityError as e:
        if "Duplicate entry" in e._message():
            return HTTPException(status_code=409, detail="Conflicted")
        return HTTPException(status_code=400, detail="Bad Request")
    return resp


async def get_background(
    db: AsyncSession,
    name: str,
) -> GetBackgroundResponse:
    """背景を取得します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db, select(BackgroundSave).filter(BackgroundSave.userId == name)
    )
    item = BackgroundReqResp.from_orm(background_db)
    resp = GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def edit_background(
    db: AsyncSession,
    name: str,
    model: BackgroundReqResp,
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
    update_data = model.dict(exclude_unset=True)
    background_db.updatedTime = get_current_unix()
    EXCLUDES = [
        "id",
        "userId",
        "createdTime",
        "updatedTime",
    ]
    for k in EXCLUDES:
        update_data.pop(k, None)
    for k in update_data.keys():
        setattr(background_db, k, update_data[k])
    try:
        await db.commit()
        await db.refresh(background_db)
    except sqlalchemy.exc.IntegrityError as e:
        if "Duplicate entry" in e._message():
            return HTTPException(status_code=409, detail="Conflicted")
        return HTTPException(status_code=400, detail="Bad Request")
    item = BackgroundReqResp.from_orm(background_db)
    resp = GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


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
    db.add(background_db)
    await db.commit()
    await db.refresh(background_db)
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
    return GetBackgroundListResponse(
        users=resp.items,
        total=resp.total,
        pages=resp.pageCount,
    )
