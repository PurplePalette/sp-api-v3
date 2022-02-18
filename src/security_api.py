# coding: utf-8

import base64
import datetime
import json
import os
from os.path import dirname, join
from typing import Dict, Optional  # noqa: F401

import firebase_admin
from dotenv import load_dotenv
from fastapi import Header, HTTPException, Request
from fastapi.responses import JSONResponse
from firebase_admin import auth
from src.models.start_session_request import StartSessionRequest

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DUMMY_USER: Dict[str, str] = {
    "user_id": "hoge",
    "email": "hoge@example.com",
}

dependsHeader = Header(None)


env_cred = os.environ.get("FIREBASE_CRED")

if not env_cred:
    raise Exception("No FIREBASE_CRED environment variable found")

cred_dict = json.loads(base64.b64decode(env_cred).decode())
cred = firebase_admin.credentials.Certificate(cred_dict)
default_app = firebase_admin.initialize_app(cred)


async def get_current_user_stub(
    authorization: Optional[str] = dependsHeader,
) -> Dict[str, str]:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        raise HTTPException(status_code=401, detail="Not verified")
    DUMMY_USER["user_id"] = separated_authorization[1]
    return DUMMY_USER


async def get_current_user_optional_stub(
    authorization: Optional[str] = dependsHeader,
) -> Optional[Dict[str, str]]:
    if authorization is None:
        return None
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        return None
    DUMMY_USER["user_id"] = separated_authorization[1]
    return DUMMY_USER


def start_session(req: StartSessionRequest) -> JSONResponse:
    """Firebase セッションクッキーを生成する"""
    try:
        expires_in = datetime.timedelta(days=14)
        session_cookie = auth.create_session_cookie(
            req.idToken, expires_in=expires_in, app=default_app
        )
        resp = JSONResponse({"message": "Baked new cookies"})
        resp.set_cookie(
            key="session",
            value=session_cookie,
            max_age=int(expires_in.total_seconds()),
            expires=int(expires_in.total_seconds()),
            httponly=True,
            secure=True,
        )
        return resp
    except firebase_admin.exceptions.FirebaseError:
        return JSONResponse({"message": "Failed to bake new cookies"}, status_code=400)


def get_current_user(request: Request) -> Dict[str, str]:
    session_cookie = request.cookies.get("session")
    if not session_cookie:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        decoded_claims: Dict[str, str] = auth.verify_session_cookie(
            session_cookie, check_revoked=True
        )
        decoded_claims["user_id"] = decoded_claims["uid"]
        return decoded_claims
    except auth.InvalidSessionCookieError:
        raise HTTPException(status_code=401, detail="Not verified")


def get_current_user_optional(request: Request) -> Optional[Dict[str, str]]:
    session_cookie = request.cookies.get("session")
    if not session_cookie:
        return None
    try:
        decoded_claims: Dict[str, str] = auth.verify_session_cookie(
            session_cookie, check_revoked=True
        )
        decoded_claims["user_id"] = decoded_claims["uid"]
        return decoded_claims
    except auth.InvalidSessionCookieError:
        return None


def end_session() -> JSONResponse:
    """Firebase セッションクッキーを失効させる"""
    resp = JSONResponse({"message": "Now you ate cookies"})
    resp.set_cookie("session", max_age=0, expires=0)
    return resp
