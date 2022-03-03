import time

from shortuuid import ShortUUID
from src.config import CDN_ENDPOINT
from src.models import SonolusResourceLocator


def create_srl(resource_type: str, hash: str) -> str:
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
