from enum import Enum
from typing import TypedDict

import httpx
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import IMAGE_SERVICE_ENDPOINT
from src.cruds.utils.db import get_first_item_or_error, save_to_db
from src.cruds.utils.funcs import get_current_unix
from src.cruds.utils.ids import get_internal_id
from src.database.objects.file_map import FileMap
from src.database.objects.upload import Upload as UploadSave


class ImageProcessException(Exception):
    """レベル変換失敗例外型"""

    pass


class ImageProcessResponse(TypedDict):
    """レベル変換応答型"""

    hash: str


class ImageProcessStatus(Enum):
    """レベル変換ステータス定数"""

    # 処理中
    PROCESSING = 0
    # 変換済み
    COMPLETED = 1
    # 変換失敗
    FAILED = -1


class ImageProcessTask:
    """
    外部APIのsonolus-image-serverを使って譜面変換を行うタスク
    """

    status: ImageProcessStatus = ImageProcessStatus.PROCESSING
    db: AsyncSession
    type_: str
    hash: str
    user_display_id: str

    def __init__(
        self, db: AsyncSession, type_: str, hash: str, user_display_id: str
    ) -> None:
        self.status = ImageProcessStatus.PROCESSING
        self.db = db
        self.type = type_
        self.hash = hash
        self.user_display_id = user_display_id
        print("ImageProcess task initialized.")

    async def __call__(self) -> None:
        """バックグラウンドタスクとして実行されるメソッド"""
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{IMAGE_SERVICE_ENDPOINT}/convert",
                    json={"type": self.type, "hash": self.hash},
                )
                # 連携先がエラーを吐くと LevelConversionException
                if resp.status_code != 200:
                    raise ImageProcessException(f"{resp.status_code}: {resp.text}")
                resp_json: ImageProcessResponse = resp.json()
                internal_id = await get_internal_id(self.db, self.user_display_id)
                now = get_current_unix()
                sha1_hash = resp_json["hash"]
                # DBが要素が無いとエラーを吐いた場合 HTTPException
                image_upload: UploadSave = await get_first_item_or_error(
                    self.db,
                    select(UploadSave).filter(UploadSave.objectHash == self.hash),
                    HTTPException(status_code=404, detail="Not Found"),
                )
                level_upload = UploadSave(
                    createdTime=now,
                    updatedTime=now,
                    objectType=self.type,
                    objectSize=image_upload.objectSize,
                    objectHash=sha1_hash,
                    objectName=image_upload.objectName,
                    objectTargetType="level",
                    objectTargetId=None,
                    userId=internal_id,
                )
                await save_to_db(self.db, level_upload)
                file_map = FileMap(
                    createdTime=now,
                    beforeType=self.type,
                    beforeHash=self.hash,
                    afterType=self.type,
                    afterHash=sha1_hash,
                    processType="ImageProcess",
                )
                await save_to_db(self.db, file_map)
        except ImageProcessException as e:
            print("画像処理/連携先サーバー側エラー:", e)
            self.status = ImageProcessStatus.FAILED
        except HTTPException as e:
            print("画像処理/サーバーDB側エラー:", e)
            self.status = ImageProcessStatus.FAILED
        else:
            print("画像処理/変換できたらしい")
            self.status = ImageProcessStatus.COMPLETED

    def get_status(self) -> ImageProcessStatus:
        return self.status
