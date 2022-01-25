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
from src.apis.depends import dependsPath
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_level_response import GetLevelResponse

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/levels/rating_decrease_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Vote for decrease rating on a level",
)
async def decrease_rating(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
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
    tags=["accounts_levels_specials"],
    summary="Favorite level",
)
async def favorite_level(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
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
    tags=["accounts_levels_specials"],
    summary="Get announce",
)
async def get_account_announce(
    accountKey: str = dependsPath,
    announceName: str = dependsPath,
) -> GetLevelResponse:
    """指定されたアナウンス情報を表示します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/announce",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Get announce list",
)
async def get_account_announce_list(
    accountKey: str = dependsPath,
) -> GetLevelResponse:
    """現在のアナウンス一覧を取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/debut",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["accounts_levels_specials"],
    summary="Get debut levels",
)
async def get_account_debut_levels(
    accountKey: str = dependsPath,
) -> GetLevelResponse:
    """新規譜面作者の譜面のみを返すエンドポイント"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/mylist",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Get mylist",
)
async def get_account_mylist(
    accountKey: str = dependsPath,
) -> GetLevelResponse:
    """対象の鍵を持つユーザーのマイリストを取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/pickups",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
    },
    tags=["accounts_levels_specials"],
    summary="Get pickup levels",
)
async def get_account_pickup_levels(
    accountKey: str = dependsPath,
) -> GetLevelResponse:
    """管理者の指定したおすすめ譜面などを返すエンドポイント"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/random",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Get a random level",
)
async def get_account_random(
    accountKey: str = dependsPath,
) -> GetLevelResponse:
    """ランダムな譜面を取得します"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/flick_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Get flick level",
)
async def get_flick_level(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
) -> GetLevelResponse:
    """譜面のノーツ部分をゴリ押しでフリックのみに差し替えた特殊な譜面を取得する"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/rating_increase_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Vote for increase rating on a level",
)
async def increase_rating(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/levels/like_{levelName}",
    responses={
        200: {"model": GetLevelResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_levels_specials"],
    summary="Like a level",
)
async def rate_level(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
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
    tags=["accounts_levels_specials"],
    summary="Unfavorite level",
)
async def unfavorite_level(
    accountKey: str = dependsPath,
    levelName: str = dependsPath,
) -> GetLevelResponse:
    """It returns specified level info.
    It will raise 404 if the level is not registered in this server"""
    ...
