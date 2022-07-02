import time

from shortuuid import ShortUUID
from src.config import CDN_ENDPOINT, PREFIX
from src.models import SonolusResourceLocator


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
    new_name = obj_name
    if obj_name.startswith(PREFIX):
        new_name = obj_name[len(PREFIX) :]
    return new_name
