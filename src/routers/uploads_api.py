# coding: utf-8
from fastapi import APIRouter, BackgroundTasks, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.extras.upload import upload_process
from src.models.post_upload_response import PostUploadResponse
from src.routers.depends import (
    dependsDatabase,
    dependsFile,
    dependsFileSize,
    dependsFirebase,
    dependsForm,
)
from src.security_api import FirebaseClaims

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
    response_model=PostUploadResponse,
)
async def upload_file(
    background_tasks: BackgroundTasks,
    type: str = dependsForm,
    file: UploadFile = dependsFile,
    file_size: int = dependsFileSize,
    db: AsyncSession = dependsDatabase,
    user: FirebaseClaims = dependsFirebase,
) -> PostUploadResponse:
    """ファイルのアップロードを受け付ける (投稿から1時間以上使用されないファイルは自動削除したい)"""
    return await upload_process(type, file, file_size, db, user, background_tasks)
