# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
)
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import (
    dependsBody,
    dependsDatabase,
    dependsFirebase,
    dependsFirebaseOptional,
    dependsPage,
    dependsPath,
)
from src.cruds.user import create_user as crud_create
from src.cruds.user import delete_user as crud_delete  # noqa: F401
from src.cruds.user import edit_user as crud_edit  # noqa: F401
from src.cruds.user import get_user as crud_get  # noqa: F401
from src.cruds.user import list_user as crud_list  # noqa: F401
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_user_list_response import GetUserListResponse
from src.models.user import User

router = APIRouter()


@router.post(
    "/users",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        409: {"description": "Conflict"},
    },
    tags=["users"],
    summary="Add a user",
)
async def add_user(
    user: User = dependsBody,
    db: AsyncSession = dependsDatabase,
    auth: FirebaseClaims = dependsFirebase,
) -> User:
    """Add specified new user to server"""
    return await crud_create(db, user, auth)


@router.delete(
    "/users/{userId}",
    responses={
        200: {"description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        409: {"description": "Conflict"},
    },
    tags=["users"],
    summary="Delete a user",
)
async def delete_user(
    userId: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> None:
    """指定したユーザーを削除します"""
    await crud_delete(db, user)
    return None


@router.patch(
    "/users/{userId}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Edit a user",
)
async def edit_user(
    userId: str = dependsPath,
    user: User = dependsBody,
    db: AsyncSession = dependsDatabase,
    auth: FirebaseClaims = dependsFirebase,
) -> User:
    """指定したuser情報を編集します"""
    return await crud_edit(db, userId, user, auth)


@router.get(
    "/users/list",
    responses={
        200: {"model": GetUserListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get user list",
    response_model=GetUserListResponse,
)
async def get_user_list(
    page: int = dependsPage,
    db: AsyncSession = dependsDatabase,
) -> GetUserListResponse:
    """サーバーに登録されたユーザー一覧を返します"""
    return await crud_list(db, page)


@router.get(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get a user",
)
async def get_user(
    userId: str = dependsPath,
    db: AsyncSession = dependsDatabase,
    auth: Optional[FirebaseClaims] = dependsFirebaseOptional,
) -> User:
    """指定したユーザー情報を取得します"""
    return await crud_get(db, userId, auth)
