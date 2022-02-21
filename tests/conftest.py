import asyncio
import os
import sys
from os.path import dirname, join
from typing import AsyncGenerator, Generator

import pytest_asyncio
import requests
from dotenv import load_dotenv
from firebase_admin import auth
from firebase_admin.auth import EmailAlreadyExistsError
from httpx import AsyncClient
from seeder import patch_open, seed
from src.database.db import Base, engine
from src.main import app as application
from src.security_api import (
    default_app,
    get_current_user,
    get_current_user_optional,
    get_current_user_optional_stub,
    get_current_user_stub,
)

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

IS_LOCAL = os.environ.get("IS_LOCAL")

TEST_FILE_ENDPOINT = "https://cdn.purplepalette.net/file/potato-test"

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
        if not IS_LOCAL:
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
        try:
            user = auth.create_user(
                display_name="KafuuChino",
                email="user@example.com",
                password="password",
                app=default_app,
            )
            resp = requests.post(
                "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake",
                json={"email": "user@example.com", "password": "password"},
            ).json()
            print("User created:", user.uid)
            print("User idToken:", resp["idToken"])
        except EmailAlreadyExistsError:
            pass
        yield
