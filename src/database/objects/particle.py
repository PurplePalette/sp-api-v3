from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Particle(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "particles"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    texture = Column(String(128))
    engines = relationship("Engine", back_populates="particle")
    levels = relationship("Level", back_populates="particle")
    user = relationship("User", back_populates="particles", uselist=False)
