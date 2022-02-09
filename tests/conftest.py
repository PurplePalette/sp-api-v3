import asyncio
import sys
from typing import AsyncGenerator, Generator

import pytest_asyncio
from httpx import AsyncClient
from seeder import patch_open, seed
from src.database.db import Base, engine
from src.main import app as application
from src.security_api import (
    get_current_user,
    get_current_user_optional,
    get_current_user_optional_stub,
    get_current_user_stub,
)

"""
Based on async-fastapi-sqlalchemy
https://github.com/rhoboro/async-fastapi-sqlalchemy/blob/main/app/tests/conftest.py

And fix from pytest-async-sqlalchemy
https://github.com/igortg/pytest-async-sqlalchemy#providing-a-session-scoped-event-loop
"""


@pytest_asyncio.fixture
async def client() -> AsyncGenerator:
    application.dependency_overrides[get_current_user] = get_current_user_stub
    application.dependency_overrides[
        get_current_user_optional
    ] = get_current_user_optional_stub
    async with AsyncClient(app=application, base_url="https://test") as c:
        yield c


@pytest_asyncio.fixture(scope="session")
def event_loop() -> Generator:
    """
    Creates an instance of the default event loop for the test session.
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        # Avoid "RuntimeError: Event loop is closed" on Windows when tearing down tests
        # https://github.com/encode/httpx/issues/914
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
def setup_test_db() -> Generator:
    with engine.begin():
        print("Dropping database...")
        Base.metadata.drop_all(bind=engine)
        print("Dropped database!")
        print("Creating database...")
        Base.metadata.create_all(bind=engine)
        print("Created database!")
        patch_open()
        print("Seeding database...")
        seed()
        print("Seeded database!")
        yield
