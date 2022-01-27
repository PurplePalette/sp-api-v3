from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Engine(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "engines"
    __table_args__ = {"extend_existing": True}

    thumbnailHash = Column(String(128))
    dataHash = Column(String(128))
    configurationHash = Column(String(128))
    backgroundId = Column(Integer, ForeignKey("backgrounds.id"))
    effectId = Column(Integer, ForeignKey("effects.id"))
    particleId = Column(Integer, ForeignKey("particles.id"))
    skinId = Column(Integer, ForeignKey("skins.id"))
    background = relationship("Background", back_populates="engines", uselist=False)
    effect = relationship("Effect", back_populates="engines", uselist=False)
    particle = relationship("Particle", back_populates="engines", uselist=False)
    skin = relationship("Skin", back_populates="engines", uselist=False)
    levels = relationship("Level", back_populates="engine")
    user = relationship("User", back_populates="engines", uselist=False)
