from db import Base
from mixins import SonolusDataMixin, TimeMixin
from sqlalchemy import Column, String


class Announce(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "announces"
    __table_args__ = {"extend_existing": True}

    coverHash = Column(String(128), nullable=True)
    bgmHash = Column(String(128), nullable=True)
    dataHash = Column(String(128), nullable=True)
