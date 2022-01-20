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
    "/tests/{testId}/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing background",
)
async def get_background_test(
    testId: str = defaultPath,
    backgroundName: str = defaultPath,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/effects/{effectName}",
    responses={
        200: {"model": GetEffectResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing effect",
)
async def get_effect_test(
    testId: str = defaultPath,
    effectName: str = defaultPath,
) -> GetEffectResponse:
    """It returns specified effect info.
    It will raise 404 if the effect is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/engines/{engineName}",
    responses={
        200: {"model": GetEngineResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing engine",
)
async def get_engine_test(
    testId: str = defaultPath,
    engineName: str = defaultPath,
) -> GetEngineResponse:
    """It returns specified engine info.
    It will raise 404 if the engine is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/levels/{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing level",
)
async def get_level_test(
    testId: str = defaultPath,
    levelName: str = defaultPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/particles/{particleName}",
    responses={
        200: {"model": GetParticleResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing particle",
)
async def get_particle_test(
    testId: str = defaultPath,
    particleName: str = defaultPath,
) -> GetParticleResponse:
    """It returns specified particle info.
    It will raise 404 if the particle is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["tests"],
    summary="Get testing skin",
)
async def get_skin_test(
    testId: str = defaultPath,
    skinName: str = defaultPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/tests/{testId}/info",
    responses={
        200: {"model": ServerInfo, "description": "OK"},
    },
    tags=["tests"],
    summary="Get user server info",
)
async def get_test_server_info(
    testId: str = defaultPath,
) -> ServerInfo:
    """テスト個別の情報一覧を返します"""
    ...


@router.get(
    "/tests/{testId}/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get backgrounds for test",
)
async def get_tests_backgrounds(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetBackgroundListResponse:
    """譜面テスト用エンドポイント/ 背景一覧を返す(一般の背景リストと同じのが返される)"""
    ...


@router.get(
    "/tests/{testId}/effects/list",
    responses={
        200: {"model": GetEffectListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get effects for test",
)
async def get_tests_effects(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEffectListResponse:
    """譜面テスト用エンドポイント/ エフェクト一覧を返す(一般のエフェクトリストと同じのが返される)"""
    ...


@router.get(
    "/tests/{testId}/engines/list",
    responses={
        200: {"model": GetEngineListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get engines for test",
)
async def get_tests_engines(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetEngineListResponse:
    """譜面テスト用エンドポイント/ エンジン一覧を返す(一般のエンジンリストと同じのが返される)"""
    ...


@router.get(
    "/tests/{testId}/levels/list",
    responses={
        200: {"model": GetLevelListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get levels for test",
)
async def get_tests_levels(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetLevelListResponse:
    """譜面テスト用エンドポイント/ 背景一覧を返す"""
    ...


@router.get(
    "/tests/{testId}/particles/list",
    responses={
        200: {"model": GetParticleListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get particles for test",
)
async def get_tests_particles(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetParticleListResponse:
    """譜面テスト用エンドポイント/ パーティクル一覧を返す(一般の背景リストと同じのが返される)"""
    ...


@router.get(
    "/tests/{testId}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["tests"],
    summary="Get skins for test",
)
async def get_tests_skins(
    testId: str = defaultPath,
    localization: str = defaultLocalization,
    page: int = defaultPage,
    keywords: str = defaultKeywords,
) -> GetSkinListResponse:
    """譜面テスト用エンドポイント/ スキン一覧を返す(一般のスキンリストと同じのが返される)"""
    ...
