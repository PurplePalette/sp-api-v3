from datetime import datetime

from sqlalchemy import Column, String
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Announce(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "announces"
    __table_args__ = {"extend_existing": True}

    # FIXME: Remove this init and use better mypy config
    def __init__(
        self,
        name: str,
        title: str,
        title_en: str,
        artists: str,
        artists_en: str,
        author: str,
        author_en: str,
        description: str,
        description_en: str,
        public: bool,
        created_time: datetime,
        updated_time: datetime,
        coverHash: str,
        bgmHash: str,
        dataHash: str,
        user_id: int,
    ) -> None:
        self.name = name
        self.title = title
        self.title_en = title_en
        self.artists = artists
        self.artists_en = artists_en
        self.author = author
        self.author_en = author_en
        self.description = description
        self.description_en = description_en
        self.public = public
        self.created_time = created_time
        self.updated_time = updated_time
        self.coverHash = coverHash
        self.bgmHash = bgmHash
        self.dataHash = dataHash
        self.user_id = user_id
        super().__init__()

    coverHash = Column(String(128), nullable=True)
    bgmHash = Column(String(128), nullable=True)
    dataHash = Column(String(128), nullable=True)
