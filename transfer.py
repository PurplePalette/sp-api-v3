# coding: utf-8
import asyncio
from dataclasses import dataclass
import json
import os
import os.path
import glob
from sqlalchemy.orm import sessionmaker
from typing import Any, Dict, List
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from dotenv import load_dotenv
from src.cruds.utils import get_first_item_or_error, get_internal_id
from src.database.objects import UserSave, LevelSave, GenreSave
from src.database.db import async_session, async_engine


@dataclass
class OldLevel:
    info: Dict[str, Any]
    bgm: bytes
    cover: bytes
    data: bytes
    sus: bytes


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
    for data_name in ["bgm.mp3", "cover.png", "data.gz", "data.sus"]:
        with open(os.path.join(path, data_name), "rb") as g:
            files.append(g.read())
    return OldLevel(info, files[0], files[1], files[2], files[3])


async def add_user(sessionmaker: sessionmaker, userDict: Dict[Any, str]):
    """Add dict user to database"""
    async with sessionmaker() as db:
        userDict.pop("totalFumen", None)
        user = UserSave(**userDict)
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


async def add_level(sessionmaker: sessionmaker, level: OldLevel):
    """Add dict user to database"""
    async with sessionmaker() as db:
        user_id = await get_internal_id(db, level.info["userId"])
        genre = await get_first_item_or_error(
            db, select(GenreSave).where(GenreSave.name == level.info["genre"])
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
            engineId=1,
            genreId=genre.id,
            userId=user_id,
        )
        db.add(level_db)
        db.add()
        try:
            await db.commit()
            await db.refresh(level_db)
        except IntegrityError as e:
            if "Duplicate entry" in e._message():
                print(f"Level {level.info['name']} already exists")
            else:
                print(e._message())
        # TODO: Import level/sus/bgm/cover binary to server
        # Need UploadApi...


async def main():
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
    users_path = [os.path.join(users_folder, p) for p in users_path]
    print("Loading users...")
    users = load_users(users_path)
    print("Adding users...")
    # AsyncなDBを取得
    await asyncio.gather(*[add_user(async_session, user) for user in users])
    await async_engine.dispose()
    """
    # レベルの移行
    levels_path = os.listdir(levels_folder)
    if ".gitkeep" in levels_path:
        levels_path.remove(".gitkeep")
    levels_path = [os.path.join(levels_folder, p) for p in levels_path]
    for level_path in levels_path:
        level = load_level(level_path)
        await add_level(db, level)
    """


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
