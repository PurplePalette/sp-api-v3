# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)
from src.apis.defaults import (
    defaultBody,
    defaultKeywords,
    defaultLocalization,
    defaultPage,
    defaultPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.get_effect_list_response import GetEffectListResponse
from src.models.get_effect_response import GetEffectResponse
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.get_particle_list_response import GetParticleListResponse
from src.models.get_particle_response import GetParticleResponse
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse
from src.models.get_user_list_response import GetUserListResponse
from src.models.server_info import ServerInfo
from src.models.user import User

router = APIRouter()


@router.delete(
    "/users/{userId}",
    responses={
        200: {"description": "OK"},
    },
    tags=["users"],
    summary="Delete user",
)
async def delete_user(
    userId: str = defaultPath,
) -> None:
    """指定したユーザーを削除します"""
    ...


@router.patch(
    "/users/{userId}",
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Edit user",
)
async def edit_user(
    userId: str = defaultPath,
    user: User = defaultBody,
) -> None:
    """指定したuser情報を編集します"""
    ...


@router.get(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get user",
)
async def get_user(
    userId: str = defaultPath,
) -> User:
    """指定したユーザー情報を取得します"""
    ...


@router.get(
    "/users/list",
    responses={
        200: {"model": GetUserListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get user list",
)
async def get_user_list() -> GetUserListResponse:
    """サーバーに登録されたユーザー一覧を返します"""
    ...


@router.get(
    "/users/{userId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["users"],
    summary="Get user server info",
)
async def get_user_server_info(
    userId: str = defaultPath,
) -> ServerInfo:
    """ユーザー個別の情報一覧を返します"""
    ...


@router.get(
    "/users/{userId}/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users background",
)
async def get_users_background(
    userId: str = defaultPath,
    backgroundName: str = defaultPath,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get backgrounds for test",
)
async def get_users_backgrounds(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetBackgroundListResponse:
    """ユーザー個別用エンドポイント/ 背景一覧を返す"""
    ...


@router.get(
    "/users/{userId}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users effect",
)
async def get_users_effect(
    userId: str = defaultPath,
    effectName: str = defaultPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get effects for test",
)
async def get_users_effects(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEffectListResponse:
    """ユーザー個別用エンドポイント/ エフェクト一覧を返す"""
    ...


@router.get(
    "/users/{userId}/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users engine",
)
async def get_users_engine(
    userId: str = defaultPath,
    engineName: str = defaultPath,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get engines for test",
)
async def get_users_engines(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEngineListResponse:
    """ユーザー個別用エンドポイント/ エンジン一覧を返す"""
    ...


@router.get(
    "/users/{userId}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users level",
)
async def get_users_level(
    userId: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get levels for test",
)
async def get_users_levels(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetLevelListResponse:
    """ユーザー個別用エンドポイント/ 背景一覧を返す"""
    ...


@router.get(
    "/users/{userId}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users particle",
)
async def get_users_particle(
    userId: str = defaultPath,
    particleName: str = defaultPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get particles for test",
)
async def get_users_particles(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetParticleListResponse:
    """ユーザー個別用エンドポイント/ パーティクル一覧を返す"""
    ...


@router.get(
    "/users/{userId}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users"],
    summary="Get users skin",
)
async def get_users_skin(
    userId: str = defaultPath,
    skinName: str = defaultPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["users"],
    summary="Get skins for test",
)
async def get_users_skins(
    userId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetSkinListResponse:
    """ユーザー個別用エンドポイント/ スキン一覧を返す"""
    ...
