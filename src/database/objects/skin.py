from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Skin(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "skins"
    __table_args__ = {"extend_existing": True}

    thumbnailHash = Column(String(128))
    dataHash = Column(String(128))
    textureHash = Column(String(128))
    engines = relationship("Engine", back_populates="skin")
    levels = relationship("Level", back_populates="skin")
