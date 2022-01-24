from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Background(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "backgrounds"
    __table_args__ = {"extend_existing": True}

    thumbnailHash = Column(String(128))
    dataHash = Column(String(128))
    imageHash = Column(String(128))
    engines = relationship("Engine", back_populates="background")
    levels = relationship("Level", back_populates="background")
