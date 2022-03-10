# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.extras.user import UserCrud
from src.models.add_user_request import AddUserRequest
from src.models.get_user_list_response import GetUserListResponse
from src.models.start_session_request import StartSessionRequest
from src.models.user import User
from src.routers.depends import (
    dependsAddUser,
    dependsBody,
    dependsDatabase,
    dependsFirebase,
    dependsFirebaseOptional,
    dependsPage,
    dependsPath,
    dependsStartSession,
)
from src.security_api import start_session

router = APIRouter()
crud = UserCrud()


@router.post(
    "/users/session",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
    },
    tags=["users"],
    summary="Start a session",
)
def add_session(
    req: StartSessionRequest = dependsStartSession,
) -> JSONResponse:
    """Add specified new user to server"""
    resp: JSONResponse = start_session(req)
    return resp


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
    db: AsyncSession = dependsDatabase,
    req: AddUserRequest = dependsAddUser,
) -> User:
    """Add specified new user to server"""
    return await crud.add(db, req)


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
    await crud.delete(db, userId, user)
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
    return await crud.edit(db, user, auth)


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
    return await crud.list(db, page)


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
    return await crud.get(db, userId, auth)
