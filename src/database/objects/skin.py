from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Skin(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "skins"
    __table_args__ = {"extend_existing": True}

    thumbnail_hash = Column(String(128))
    data_hash = Column(String(128))
    texture_hash = Column(String(128))
    engines = relationship("Engine", back_populates="skin")
    levels = relationship("Level", back_populates="skin")
    user = relationship("User", back_populates="skins", uselist=False)
