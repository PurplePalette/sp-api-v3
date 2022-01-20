from typing import Union

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.main import app as application
from starlette.testclient import ASGI2App, ASGI3App


@pytest.fixture
def app() -> FastAPI:
    application.dependency_overrides = {}
    return application  # type: ignore


@pytest.fixture
def client(app: Union[ASGI2App, ASGI3App]) -> TestClient:
    return TestClient(app)
