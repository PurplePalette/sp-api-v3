# coding: utf-8

import base64
import datetime
import json
import os
from dataclasses import dataclass
from os.path import dirname, join
from typing import Dict, Optional

import firebase_admin
import httpx
from dotenv import load_dotenv
from fastapi import Header, HTTPException
from fastapi.responses import JSONResponse
from firebase_admin import auth
from src.models.start_session_request import StartSessionRequest

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

dependsHeader = Header(None)

env_cred = os.environ.get("FIREBASE_CRED")

if not env_cred:
    raise Exception("No FIREBASE_CRED environment variable found")

cred_dict = json.loads(base64.b64decode(env_cred).decode())
cred = firebase_admin.credentials.Certificate(cred_dict)
default_app = firebase_admin.initialize_app(cred)


@dataclass
class FirebaseClaims:
    user_id: str
    email: str


def start_session(req: StartSessionRequest) -> JSONResponse:
    """Firebase セッションクッキーを生成する"""
    try:
        expires_in = datetime.timedelta(days=14)
        session_cookie = auth.create_session_cookie(
            req.idToken, expires_in=expires_in, app=default_app
        )
        return JSONResponse(
            {
                "session": session_cookie,
                "message": "Baked new cookies",
            }
        )
    except firebase_admin.exceptions.FirebaseError:
        return JSONResponse({"message": "Failed to bake new cookies"}, status_code=400)


def __get_current_user(
    authorization: Optional[str],
) -> Optional[Dict[str, str]]:
    """セッションクッキーを検証しclaimsを返す、検証できない場合はNoneを返す"""
    if not authorization:
        return None
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        return None
    session_cookie = separated_authorization[1]
    try:
        decoded_claims: Dict[str, str] = auth.verify_session_cookie(
            session_cookie, check_revoked=True
        )
        decoded_claims["user_id"] = decoded_claims["uid"]
        return decoded_claims
    except auth.InvalidSessionCookieError:
        return None


def get_current_user(authorization: Optional[str] = dependsHeader) -> Dict[str, str]:
    """セッションクッキーからユーザー情報を取得する、取得できない場合はエラーを返す"""
    resp = __get_current_user(authorization)
    if resp is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return resp


def get_current_user_optional(
    authorization: Optional[str] = dependsHeader,
) -> Optional[Dict[str, str]]:
    """セッションクッキーからユーザー情報を取得する、取得できない場合はNoneを返す"""
    return __get_current_user(authorization)


DUMMY_USER: Dict[str, str] = {
    "user_id": "hoge",
    "email": "hoge@example.com",
}


async def get_current_user_stub(
    authorization: Optional[str] = dependsHeader,
) -> Dict[str, str]:
    """現在ログイン中のユーザー情報を取得するスタブ、取得できない場合はエラーを返す"""
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
    """現在ログイン中のユーザー情報を取得するスタブ、取得できない場合はNoneを返す"""
    if authorization is None:
        return None
    separated_authorization = authorization.split("Bearer ")
    if len(separated_authorization) != 2:
        return None
    DUMMY_USER["user_id"] = separated_authorization[1]
    return DUMMY_USER


def get_id_token_from_emulator(endpoint: str, email: str, password: str) -> str:
    """IDトークンを発行する(Firebase Emulator Suiteでのみ使用可能)"""
    resp = httpx.post(
        f"{endpoint}/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword",
        params={"key": "dummy"},
        json={"email": email, "password": password},
    )
    if resp.status_code != 200:
        raise Exception(f"Failed to get idToken: {resp.text}")
    return resp.json()["idToken"]
