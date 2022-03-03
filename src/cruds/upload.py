import gzip
from dataclasses import dataclass
from hashlib import sha1
from io import StringIO
from re import finditer
from typing import List

from fastapi import HTTPException, UploadFile
from fastapi_cloudauth.firebase import FirebaseClaims
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.utils import get_current_unix, get_internal_id, save_to_db
from src.database.bucket import get_bucket
from src.database.objects import UploadSave
from src.models.post_upload_response import PostUploadResponse


@dataclass
class AcceptableType:
    """アップロード可能なファイルタイプ"""

    srl_name: str
    content_type: str
    maximum_size: int


# 受け付ける 画像型のSRL
IMAGE_TYPES = [
    AcceptableType(
        srl_name,
        "image/png",
        10 * 1024 * 1024,
    )
    for srl_name in [
        "LevelCover",
        "BackgroundImage",
        "BackgroundThumbnail",
        "EngineThumbnail",
        "EffectThumbnail",
        "SkinThumbnail",
        "ParticleThumbnail",
        "SkinTexture",
        "ParticleTexture",
        "SkinTexture",
    ]
]

# 受け付ける MP3型のSRL
AUDIO_TYPES = [
    AcceptableType(
        srl_name,
        "audio/mpeg",
        50 * 1024 * 1024,
    )
    for srl_name in ["LevelPreview", "LevelBgm"]
]

# 受け付ける JSON型のSRL
DATA_TYPES = [
    AcceptableType(
        srl_name,
        "application/json",
        5 * 1024 * 1024,
    )
    for srl_name in [
        "BackgroundData",
        "EffectData",
        "EngineData",
        "ParticleData",
        "SkinData",
        "LevelData",
        "EngineConfiguration",
    ]
]

# 受け付けるSUS型のSRL
SUS_TYPES = [
    AcceptableType(
        "SusFile",
        "text/plain",
        5 * 1024 * 1024,
    )
]

# 受付可能なファイル種別一覧(AcceptableTypeリスト)
ACCEPT_TYPES = IMAGE_TYPES + DATA_TYPES + AUDIO_TYPES + SUS_TYPES
# 受付可能なファイル種別一覧(名称リスト)
ACCEPT_TYPES_NAMES = [t.srl_name for t in ACCEPT_TYPES]


def split_by_camel(identifier: str) -> List[str]:
    """キャメルケースの文字列を分割する"""
    matches = finditer(
        ".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", identifier
    )
    return [m.group(0) for m in matches]


def get_accept_define(key: str) -> AcceptableType:
    """指定したkeyに対応するAcceptableTypeを返す"""
    if key not in ACCEPT_TYPES_NAMES:
        raise ValueError("Invalid key")
    for t in ACCEPT_TYPES:
        if t.srl_name == key:
            return t
    return ACCEPT_TYPES[0]


def compress_gzip(file: bytes) -> str:
    out = StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:  # type: ignore
        f.write(file)  # type: ignore
    return out.getvalue()


async def upload_process(
    file_type: str,
    file: UploadFile,
    file_size: int,
    db: AsyncSession,
    user: FirebaseClaims,
) -> PostUploadResponse:
    """ファイルのアップロードを受け取りバケットに登録する"""
    # 指定したファイルタイプが適切か確認
    if file_type not in ACCEPT_TYPES_NAMES:
        raise HTTPException(status_code=400, detail="Invalid file type")
    accept_define = get_accept_define(file_type)
    # 指定したファイルのCONTENT-TYPEが適切か確認
    expected_content = accept_define.content_type
    actual_content = file.content_type
    if actual_content != expected_content:
        raise HTTPException(
            status_code=400,
            detail=f"Wrong content: excepted {expected_content}, but {actual_content}",
        )
    # 指定したファイルサイズが適切か確認
    # 注意: このファイルサイズは Content-Lengthヘッダーなためあまり適切な検証ではない
    expected_size = accept_define.maximum_size
    actual_size = file_size
    if actual_size > expected_size:
        raise HTTPException(
            status_code=400,
            detail=f"Content size too big : excepted lower than {expected_size}",
        )
    # ファイルを読み出し必要ならGZip
    buf: bytes = await file.read()  # type: ignore
    if expected_content == "application/json":
        buf = compress_gzip(buf).encode("utf-8")
    # バケットにアップロード
    sha1_hash = sha1(buf).hexdigest()
    bucket = get_bucket()
    bucket.put_object(Body=buf, Key=f"{file_type}/{sha1_hash}")
    # DBに挿入
    internal_id = await get_internal_id(db, user["user_id"])
    now = get_current_unix()
    upload = UploadSave(
        createdTime=now,
        updatedTime=now,
        objectType=file_type,
        objectSize=len(buf),
        objectHash=sha1_hash,
        objectName=file.filename,
        objectTargetType=split_by_camel(file_type)[0].lower(),
        objectTargetId=None,
        userId=internal_id,
    )
    await save_to_db(db, upload)
    return PostUploadResponse(
        message="ok",
        filename=sha1_hash,
    )
