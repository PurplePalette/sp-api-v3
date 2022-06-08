# coding: utf-8
import os
from os.path import dirname, join
from typing import Any, Dict, List, Optional

import yaml
from dotenv import load_dotenv
from firebase_admin import auth
from firebase_admin.auth import EmailAlreadyExistsError
from sqlalchemy_seed import load_fixture_files, load_fixtures
from src.database.db import get_sync_db
from src.security_api import default_app

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


"""
Fix UnicodeDecodeError with monkey patch

From
https://qiita.com/ousttrue/items/527a9c3045f710806aa9
"""


def patch_open() -> None:
    """patch default file open encoding as utf8"""
    import builtins

    __original = open

    def __open(
        file: str,
        mode: str = "r",
        buffering: int = -1,
        encoding: Optional[str] = None,
        errors: Any = None,
        newline: Any = None,
        closefd: bool = True,
        opener: Any = None,
    ) -> Any:
        if "b" not in mode and not encoding:
            encoding = "utf-8"
        return __original(file, mode, buffering, encoding, errors, newline, closefd, opener)

    builtins.open = __open  # type: ignore


def seed_database() -> None:
    """Add or update database data with seed files"""
    print("Seeding database...")
    path: str = "development" if os.environ.get("IS_DEV") else "production"
    fixtures = load_fixture_files(
        os.path.join("seeds", path),
        [
            "users.yaml",
            "announces.yaml",
            "backgrounds.yaml",
            "effects.yaml",
            "particles.yaml",
            "skins.yaml",
            "engines.yaml",
            "levels.yaml",
            "genres.yaml",
            "uploads.yaml",
        ],
    )
    session = get_sync_db()
    load_fixtures(session, fixtures)
    print("Now database seeded!")


def load_firebase_users() -> List[Dict[str, str]]:
    seed_path = os.path.join("seeds", "development")
    file_path = os.path.join(seed_path, "firebase.yaml")
    with open(file_path) as f:
        firebase_users: List[Dict[str, str]] = yaml.safe_load(f)
    return firebase_users


def seed_firebase() -> None:
    """Add or update firebase data with seed files"""
    path: str = "development" if os.environ.get("IS_DEV") else "production"
    if path != "development":
        return None
    print("Seeding firebase...")
    firebase_users = load_firebase_users()
    for user in firebase_users:
        try:
            auth.create_user(
                display_name=user["display_name"],
                email=user["email"],
                password=user["password"],
                app=default_app,
            )
        except EmailAlreadyExistsError:
            pass
    print("Now firebase seeded!")


def main() -> None:
    patch_open()
    seed_database()
    seed_firebase()
