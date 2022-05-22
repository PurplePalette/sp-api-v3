import time
from os import getenv

from shortuuid import ShortUUID
from src.config import CDN_ENDPOINT
from src.models import SonolusResourceLocator

PREFIX = f'{getenv("SERVER_PREFIX")}.'


def create_srl(resource_type: str, hash: str) -> SonolusResourceLocator:
    """SonolusResourceLocatorを作成して返す"""
    url = f"{CDN_ENDPOINT}/repository/{resource_type}/{hash}"
    if "http" in CDN_ENDPOINT:
        url = hash
    return SonolusResourceLocator(
        type=resource_type,
        hash=hash,
        url=url,
    )


def get_current_unix() -> int:
    """現在のUNIX時刻を取得"""
    return int(time.time())


def get_random_name() -> str:
    """ランダムな12文字のnameを取得"""
    random_name: str = ShortUUID(
        alphabet="1234567890abcdefghijklmnopqrstuvwxyz"
    ).random(length=12)
    return random_name


def prefix_name(obj_name: str) -> str:
    """nameにプレフィックスをつける"""
    return f"{PREFIX}{obj_name}"


def remove_prefix(obj_name: str) -> str:
    """nameからプレフィックスを外す"""
    assert obj_name.startswith(PREFIX), "nameにプレフィックスがついていません"
    return obj_name[len(PREFIX) :]
