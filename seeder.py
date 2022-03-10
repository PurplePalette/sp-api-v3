# coding: utf-8
import os
from os.path import dirname, join
from typing import Any, Optional

from dotenv import load_dotenv
from sqlalchemy_seed import load_fixture_files, load_fixtures
from src.database.db import Base, get_sync_db  # noqa: F401

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
        return __original(
            file, mode, buffering, encoding, errors, newline, closefd, opener
        )

    builtins.open = __open  # type: ignore


def seed() -> None:
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


if __name__ == "__main__":
    patch_open()
    seed()
