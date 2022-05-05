# coding: utf-8
import asyncio
import glob
import json
import os
import os.path
from dataclasses import dataclass
from typing import Any, Dict, List

from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from src.cruds.extras.upload import upload_process
from src.cruds.utils import get_first_item_or_error, get_internal_id
from src.database.db import async_engine, async_session

# from src.database.objects import GenreSave, LevelSave, UserSave
from src.database.objects.level import Level as LevelSave
from src.database.objects.user import User as UserSave
from src.database.objects.genre import Genre as GenreSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave


@dataclass
class OldLevel:
    info: Dict[str, Any]
    bgm: bytes
    cover: bytes
    data: bytes
    sus: bytes


class DummyFile:
    def __init__(self, data: bytes, content_type: str, filename: str):
        self.data = data
        self.content_type = content_type
        self.filename = filename

    async def read(self):
        return self.data


class DummyBackgroundTasks:
    def __init__(self):
        self.tasks = []

    def add_task(self, func):
        self.tasks.append(func)


def load_users(path_arr: List[str]) -> List[Dict[str, Any]]:
    objs = []
    for path in path_arr:
        with open(path, "r", encoding="utf-8") as f:
            objs.append(json.load(f))
    return objs


def load_level(path: str) -> OldLevel:
    with open(os.path.join(path, "info.json"), "r", encoding="utf-8") as f:
        info = json.loads(f.read())
    files: List[bytes] = []
    for data_name in ["bgm.mp3", "cover.png", "data.json", "data.sus"]:
        with open(os.path.join(path, data_name), "rb") as g:
            files.append(g.read())
    return OldLevel(info, files[0], files[1], files[2], files[3])


async def add_user(sessionmaker: sessionmaker, user_dict: Dict[Any, str]) -> None:
    """Add dict user to database"""
    async with sessionmaker() as db:
        user_dict.pop("totalFumen", None)
        user = UserSave(**user_dict)
        db.add(user)
        try:
            await db.commit()
            await db.refresh(user)
            print(f"Import UserId {user.userId} success")
        except IntegrityError as e:
            if "Duplicate entry" in e._message():
                print(f"UserId {user.userId} already exists")
            else:
                print(e._message())
        except Exception as e:
            print("Fatal: ", e)


async def add_level(sessionmaker: sessionmaker, background_tasks: DummyBackgroundTasks, level: OldLevel) -> None:
    """Add dict user to database"""
    async with sessionmaker() as db:
        user_id = await get_internal_id(db, level.info["userId"])
        genre = await get_first_item_or_error(
            db, select(GenreSave).where(GenreSave.name == level.info["genre"]), Exception
        )
        level_db = LevelSave(
            name=level.info["name"],
            title=level.info["title"]["ja"],
            titleEn=level.info["title"]["ja"],
            subtitle=level.info["artists"]["ja"],
            subtitleEn=level.info["artists"]["ja"],
            description=level.info["description"]["ja"],
            descriptionEn=level.info["description"]["ja"],
            createdTime=level.info["createdTime"],
            updatedTime=level.info["updatedTime"],
            rating=level.info["rating"],
            cover=level.info["coverHash"],
            bgm=level.info["bgmHash"],
            data=level.info["dataHash"],
            public=level.info["public"],
            bpm=0,
            length=0,
            engineId=(
                await get_first_item_or_error(db, select(EngineSave).where(EngineSave.name == "pjsekai"), Exception)
            ).id,
            backgroundId=(
                await get_first_item_or_error(
                    db, select(BackgroundSave).where(BackgroundSave.name == "pjsekai.live"), Exception
                )
            ).id,
            effectId=(
                await get_first_item_or_error(
                    db, select(EffectSave).where(EffectSave.name == "pjsekai.classic"), Exception
                )
            ).id,
            particleId=(
                await get_first_item_or_error(
                    db, select(ParticleSave).where(ParticleSave.name == "pjsekai.classic"), Exception
                )
            ).id,
            skinId=(
                await get_first_item_or_error(
                    db, select(SkinSave).where(SkinSave.name == "pjsekai.classic"), Exception
                )
            ).id,
            genreId=genre.id,
            userId=user_id,
        )
        db.add(level_db)
        try:
            await db.commit()
            await db.refresh(level_db)
        except IntegrityError as e:
            if "Duplicate entry" in e._message():
                print(f"Level {level.info['name']} already exists")
            else:
                print(e._message())
        for data, db_type, content_type, filename in [
            (level.bgm, "LevelBgm", "audio/mpeg", "bgm.mp3"),
            (level.cover, "LevelCover", "image/png", "cover.png"),
            (level.data, "LevelData", "application/json", "data.json"),
            (level.sus, "SusFile", "text/plain", "data.sus"),
        ]:
            await upload_process(
                db_type,
                DummyFile(data, content_type, filename),
                len(data),
                db,
                {"user_id": level.info["userId"]},
                background_tasks,
            )


async def main() -> None:
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    # フォルダ読み出し
    base_folder = input("Input sonolus-uploader-core2 db folder >>")
    levels_folder = os.path.join(base_folder, "levels")
    users_folder = os.path.join(base_folder, "users")

    # 必須フォルダバリデーション
    for folder in [levels_folder, users_folder]:
        if not os.path.exists(folder):
            print(f"Required folder: {folder} not found!")
            exit(1)
    # ユーザーの移行
    users_path = glob.glob(os.path.join(users_folder, "*.json"))
    # users_path = [os.path.join(users_folder, p) for p in users_path]
    print("Loading users...")
    users = load_users(users_path)
    print("Adding users...")
    # AsyncなDBを取得
    await asyncio.gather(*[add_user(async_session, user) for user in users])
    # レベルの移行
    levels_path = os.listdir(levels_folder)
    if ".gitkeep" in levels_path:
        levels_path.remove(".gitkeep")
    levels_path = [os.path.join(levels_folder, p) for p in levels_path]
    background_tasks = DummyBackgroundTasks()
    for level_path in levels_path:
        level = load_level(level_path)
        await add_level(async_session, background_tasks, level)
    for task in background_tasks.tasks:
        await task()
    await async_engine.dispose()


if __name__ == "__main__":
    import platform

    if platform.system() == "Windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()  # type: ignore
        asyncio.set_event_loop_policy(policy)  # type: ignore
    asyncio.run(main())
