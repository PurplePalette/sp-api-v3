import gzip
import json
import os
from typing import Any, Dict

from dotenv import load_dotenv
from seeder.common import ACCEPT_MAP, DummyBackgroundTasks, DummyFile
from sqlalchemy.orm import sessionmaker
from src.cruds.extras.upload import upload_process
from src.database.db import async_engine, async_session
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave


async def add_asset(
    sessionmaker: sessionmaker,
    background_tasks: DummyBackgroundTasks,
    asset_type: type,
    asset_dict: Dict[Any, Any],
    root: str,
) -> None:
    async with sessionmaker() as db:
        item = asset_dict["item"]
        asset_hashes = {}
        for file_keys in set(item.keys()) - {
            "name",
            "version",
            "title",
            "subtitle",
            "author",
        }:
            asset_hashes[file_keys] = item[file_keys]["hash"]
            with open(root + item[file_keys]["url"], "rb") as f:
                data = f.read()
                if ACCEPT_MAP.get(item[file_keys]["type"]) == "application/json":
                    decompressed_data = json.loads(gzip.decompress(data).decode())
                    data = decompressed_data.encode("utf-8")
                await upload_process(
                    item[file_keys]["type"],
                    DummyFile(
                        data,
                        ACCEPT_MAP.get(item[file_keys]["type"], "application/octet-stream"),
                        item[file_keys]["hash"],
                    ),
                    f.tell(),
                    db,
                    {"user_id": "admin"},
                    background_tasks,
                )
        asset = asset_type(
            name=item["name"],
            title=item["title"],
            titleEn=item["title"],
            subtitle=item["subtitle"],
            subtitleEn=item["subtitle"],
            author=item["author"],
            authorEn=item["author"],
            description=asset_dict["description"],
            descriptionEn=asset_dict["description"],
            public=True,
            **asset_hashes,
        )
        db.add(asset)
        await db.commit()


async def add_engine(
    sessionmaker: sessionmaker,
    background_tasks: DummyBackgroundTasks,
    engine_dict: Dict[Any, Any],
    description: str,
) -> None:
    async with sessionmaker() as db:
        engine = EngineSave(
            name=engine_dict["name"],
            title=engine_dict["title"],
            titleEn=engine_dict["title"],
            subtitle=engine_dict["subtitle"],
            subtitleEn=engine_dict["subtitle"],
            author=engine_dict["author"],
            authorEn=engine_dict["author"],
            description=description,
            descriptionEn=description,
            data=engine_dict["data"]["hash"],
            thumbnail=engine_dict["thumbnail"]["hash"],
            configuration=engine_dict["configuration"]["hash"],
            public=True,
        )
        db.add(engine)
        await db.commit()


async def main() -> None:
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    # フォルダ読み出し
    base_folder = input("Input unarchived scp folder >> ")
    engines_folder = os.path.join(base_folder, "engines")
    effects_folder = os.path.join(base_folder, "effects")
    particles_folder = os.path.join(base_folder, "particles")
    skins_folder = os.path.join(base_folder, "skins")
    backgrounds_folder = os.path.join(base_folder, "backgrounds")
    repository_folder = os.path.join(base_folder, "repository")
    # 必須フォルダバリデーション
    for folder in [
        engines_folder,
        effects_folder,
        particles_folder,
        skins_folder,
        repository_folder,
        backgrounds_folder,
    ]:
        if not os.path.exists(folder):
            print(f"Required folder: {folder} not found!")
            exit(1)

    background_tasks: DummyBackgroundTasks = DummyBackgroundTasks()
    for save_type, folder in [
        (EffectSave, effects_folder),
        (ParticleSave, particles_folder),
        (SkinSave, skins_folder),
        (BackgroundSave, backgrounds_folder),
    ]:
        for file in os.listdir(folder):
            if file == "list":
                continue
            with open(os.path.join(folder, file)) as f:
                item = json.load(f)
                await add_asset(async_session, background_tasks, save_type, item, base_folder)

    for file in os.listdir(engines_folder):
        if file == "list":
            continue
        with open(os.path.join(engines_folder, file)) as f:
            item = json.load(f)
            await add_engine(async_session, background_tasks, item["item"], item["description"])

    for task in background_tasks.tasks:
        await task()
    await async_engine.dispose()
