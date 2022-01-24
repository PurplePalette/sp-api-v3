from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
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
        cover_hash: str,
        bgm_hash: str,
        data_hash: str,
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
        self.cover_hash = cover_hash
        self.bgm_hash = bgm_hash
        self.data_hash = data_hash
        self.user_id = user_id
        super().__init__()

    cover_hash = Column(String(128), nullable=True)
    bgm_hash = Column(String(128), nullable=True)
    data_hash = Column(String(128), nullable=True)
    user = relationship("User", back_populates="announces", uselist=False)
