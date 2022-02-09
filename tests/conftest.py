from typing import Union

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.main import app as application
from src.database.db import Base, engine
from src.security_api import (
    get_current_user,
    get_current_user_optional,
    get_current_user_optional_stub,
    get_current_user_stub,
)
from starlette.testclient import ASGI2App, ASGI3App
from seeder import patch_open, seed


def pytest_sessionstart():
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


@pytest.fixture
def app() -> FastAPI:
    application.dependency_overrides[get_current_user] = get_current_user_stub
    application.dependency_overrides[
        get_current_user_optional
    ] = get_current_user_optional_stub
    return application  # type: ignore


@pytest.fixture
def client(app: Union[ASGI2App, ASGI3App]) -> TestClient:
    return TestClient(app)
