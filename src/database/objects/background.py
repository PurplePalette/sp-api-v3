from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Background(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "backgrounds"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    image = Column(String(128))
    configuration = Column(String(128))
    engines = relationship("Engine", back_populates="background")
    levels = relationship("Level", back_populates="background")
    user = relationship("User", back_populates="backgrounds", uselist=False)
