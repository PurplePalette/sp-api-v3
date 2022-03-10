from enum import Enum
from typing import TypedDict

import httpx
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import SUS_SERVICE_ENDPOINT
from src.cruds.utils.db import get_first_item_or_error, save_to_db
from src.cruds.utils.funcs import get_current_unix
from src.cruds.utils.ids import get_internal_id
from src.database.objects.upload import Upload as UploadSave


class LevelConversionException(Exception):
    """レベル変換失敗例外型"""

    pass


class LevelConversionResponse(TypedDict):
    """レベル変換応答型"""

    hash: str


class LevelConversionStatus(Enum):
    """レベル変換ステータス定数"""

    # 処理中
    PROCESSING = 0
    # 変換済み
    COMPLETED = 1
    # 変換失敗
    FAILED = -1


class LevelConversionTask:
    """
    外部APIのsonolus-sus-serverを使って譜面変換を行うタスク
    """

    status: LevelConversionStatus = LevelConversionStatus.PROCESSING
    db: AsyncSession
    hash: str
    user_display_id: str

    def __init__(self, db: AsyncSession, hash: str, user_display_id: str) -> None:
        self.status = LevelConversionStatus.PROCESSING
        self.db = db
        self.hash = hash
        self.user_display_id = user_display_id
        print("LevelConversion task initialized.")

    async def __call__(self) -> None:
        """バックグラウンドタスクとして実行されるメソッド"""
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{SUS_SERVICE_ENDPOINT}/convert", json={"hash": self.hash}
                )
                # 連携先がエラーを吐くと LevelConversionException
                if resp.status_code != 200:
                    raise LevelConversionException(f"{resp.status_code}: {resp.text}")
                resp_json: LevelConversionResponse = resp.json()
                internal_id = await get_internal_id(self.db, self.user_display_id)
                now = get_current_unix()
                sha1_hash = resp_json["hash"]
                # DBが要素が無いとエラーを吐いた場合 HTTPException
                sus_upload: UploadSave = await get_first_item_or_error(
                    self.db,
                    select(UploadSave).filter(UploadSave.objectHash == self.hash),
                    HTTPException(status_code=404, detail="Not Found"),
                )
                level_upload = UploadSave(
                    createdTime=now,
                    updatedTime=now,
                    objectType="LevelData",
                    objectSize=sus_upload.objectSize,
                    objectHash=sha1_hash,
                    objectName=sus_upload.objectName,
                    objectTargetType="level",
                    objectTargetId=None,
                    userId=internal_id,
                )
                await save_to_db(self.db, level_upload)
        except LevelConversionException as e:
            print("連携先サーバー側エラー:", e)
            self.status = LevelConversionStatus.FAILED
        except HTTPException as e:
            print("サーバーDB側エラー:", e)
            self.status = LevelConversionStatus.FAILED
        else:
            print("変換できたらしい")
            self.status = LevelConversionStatus.COMPLETED

    def get_status(self) -> LevelConversionStatus:
        return self.status
