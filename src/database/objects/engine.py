from db import Base
from mixins import SonolusDataMixin, TimeMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Engine(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "engines"
    __table_args__ = {"extend_existing": True}

    thumbnailHash = Column(String(128))
    dataHash = Column(String(128))
    configurationHash = Column(String(128))
    background_id = Column(Integer, ForeignKey("backgrounds.id"))
    effect_id = Column(Integer, ForeignKey("effects.id"))
    particle_id = Column(Integer, ForeignKey("particles.id"))
    skin_id = Column(Integer, ForeignKey("skins.id"))
    background = relationship("Background", back_populates="engines")
    effect = relationship("Effect", back_populates="engines")
    particle = relationship("Particle", back_populates="engines")
    skin = relationship("Skin", back_populates="engines")
