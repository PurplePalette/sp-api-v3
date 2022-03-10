# coding: utf-8
import pytest
from src.database.db import async_session
from src.tasks.level_conversion import LevelConversionStatus, LevelConversionTask


@pytest.mark.asyncio
async def test_level_conversion_success() -> None:
    """Test case for level_conversion task"""
    async with async_session() as db:
        task = LevelConversionTask(db, "49.sus", "special-key")
        await task.__call__()
    assert task.status == LevelConversionStatus.COMPLETED
