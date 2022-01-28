# coding: utf-8

import os
from os.path import dirname, join
from typing import List, Optional  # noqa: F401

from dotenv import load_dotenv
from fastapi import (  # noqa: F401
    Depends,
    Header,
    HTTPException,
    Response,
    Security,
    status,
)
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows  # noqa: F401
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer  # noqa: F401
from fastapi_cloudauth.firebase import FirebaseClaims, FirebaseCurrentUser

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DUMMY_USER: FirebaseClaims = {
    "user_id": "hoge",
    "email": "hoge@example.com",
}

dependsHeader = Header(None)


async def get_current_user_stub(
    authorization: Optional[str] = dependsHeader,
) -> FirebaseClaims:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        raise HTTPException(status_code=401, detail="Not verified")
    DUMMY_USER["user_id"] = separated_authorization[1]
    return DUMMY_USER


async def get_current_user_optional_stub(
    authorization: Optional[str] = dependsHeader,
) -> FirebaseClaims:
    if authorization is None:
        return None
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        return None
    DUMMY_USER["user_id"] = separated_authorization[1]
    return DUMMY_USER


get_current_user = FirebaseCurrentUser(project_id=os.environ["PROJECT_ID"])
get_current_user_optional = FirebaseCurrentUser(
    project_id=os.environ["PROJECT_ID"], auto_error=False
)
