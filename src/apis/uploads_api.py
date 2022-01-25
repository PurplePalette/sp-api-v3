# coding: utf-8

from typing import Dict, List  # noqa: F401

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
    status,
)
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.depends import dependsDatabase, dependsFirebase, dependsForm
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.post_upload_response import PostUploadResponse

router = APIRouter()


@router.post(
    "/upload",
    responses={
        200: {"model": PostUploadResponse, "description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        413: {"description": "Request Entity Too Large"},
        429: {"description": "Too Many Requests"},
    },
    tags=["uploads"],
    summary="Upload a file",
)
async def upload_file(
    file: str = dependsForm,
    type: str = dependsForm,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> PostUploadResponse:
    """ファイルのアップロードを受け付ける (投稿から1時間以上使用されないファイルは自動削除したい)"""
    ...
