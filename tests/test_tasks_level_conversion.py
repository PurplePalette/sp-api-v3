# coding: utf-8
import pytest
from src.cruds.utils.db import save_to_db
from src.cruds.utils.funcs import get_current_unix
from src.database.bucket import get_bucket
from src.database.db import async_session
from src.database.objects.upload import Upload as UploadSave
from src.tasks.level_conversion import LevelConversionStatus, LevelConversionTask


@pytest.mark.asyncio
async def test_level_conversion_success() -> None:
    """Test case for level_conversion task"""
    bucket = get_bucket()
    sus = open("tests/assets/test.sus", "rb").read()
    bucket.put_object(Body=sus, Key="SusFile/test.sus")
    async with async_session() as db:
        now = get_current_unix()

        await save_to_db(
            db,
            UploadSave(
                userId=1,
                createdTime=now,
                updatedTime=now,
                objectType="SusFile",
                objectSize=len(sus),
                objectHash="test.sus",
                objectName="test.sus",
            ),
        )
        task = LevelConversionTask(db, "test.sus", "admin")
        await task.__call__()
    assert task.status == LevelConversionStatus.COMPLETED
