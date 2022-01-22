from db import Base
from mixins import SonolusDataMixin, TimeMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Particle(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "particles"
    __table_args__ = {"extend_existing": True}

    thumbnailHash = Column(String(128))
    dataHash = Column(String(128))
    textureHash = Column(String(128))
    engines = relationship("Engine", back_populates="particle")
    levels = relationship("Level", back_populates="particle")
