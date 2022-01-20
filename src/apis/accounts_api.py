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
from src.models.server_info import ServerInfo

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/levels/rating_decrease_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Rate level",
)
async def decrease_rating(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/favorite_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Add level to user favorite",
)
async def favorite_level(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/announce_{announceName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get announce",
)
async def get_account_announce(
    accountKey: str = defaultPath,
    announceName: str = defaultPath,
) -> GetLevelResponse:
    """指定されたアナウンス情報を表示します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/announce",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get announce list",
)
async def get_account_announce_list(
    accountKey: str = defaultPath,
) -> GetLevelResponse:
    """現在のアナウンス一覧を取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/mylist",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get mylist",
)
async def get_account_mylist(
    accountKey: str = defaultPath,
) -> GetLevelResponse:
    """対象の鍵を持つユーザーのマイリストを取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/random",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get random",
)
async def get_account_random(
    accountKey: str = defaultPath,
) -> GetLevelResponse:
    """ランダムな譜面を取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts background",
)
async def get_accounts_background(
    accountKey: str = defaultPath,
    backgroundName: str = defaultPath,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get backgrounds for test",
)
async def get_accounts_backgrounds(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetBackgroundListResponse:
    """ユーザー個別用エンドポイント/ 背景一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts effect",
)
async def get_accounts_effect(
    accountKey: str = defaultPath,
    effectName: str = defaultPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get effects for test",
)
async def get_accounts_effects(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEffectListResponse:
    """ユーザー個別用エンドポイント/ エフェクト一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts engine",
)
async def get_accounts_engine(
    accountKey: str = defaultPath,
    engineName: str = defaultPath,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get engines for test",
)
async def get_accounts_engines(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEngineListResponse:
    """ユーザー個別用エンドポイント/ エンジン一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts level",
)
async def get_accounts_level(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get levels for test",
)
async def get_accounts_levels(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetLevelListResponse:
    """ユーザー個別用エンドポイント/ 譜面一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts particle",
)
async def get_accounts_particle(
    accountKey: str = defaultPath,
    particleName: str = defaultPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get particles for test",
)
async def get_accounts_particles(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetParticleListResponse:
    """ユーザー個別用エンドポイント/ パーティクル一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get user server info",
)
async def get_accounts_server_info(
    accountKey: str = defaultPath,
) -> ServerInfo:
    """ユーザー個別の情報一覧を返します"""
    ...


@router.get(
    "/accounts/{accountKey}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get accounts skin",
)
async def get_accounts_skin(
    accountKey: str = defaultPath,
    skinName: str = defaultPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["accounts"],
    summary="Get skins for test",
)
async def get_accounts_skins(
    accountKey: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetSkinListResponse:
    """ユーザー個別用エンドポイント/ スキン一覧を返す"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/flick_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Get flick level",
)
async def get_flick_level(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """譜面のノーツ部分をゴリ押しでフリックのみに差し替えた特殊な譜面を取得する"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/rating_increase_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Rate level",
)
async def increase_rating(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/up_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Rate level",
)
async def rate_level(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/unfavorite_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts"],
    summary="Add level to user favorite",
)
async def unfavorite_level(
    accountKey: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...
