from db import Base
from mixins import SonolusDataMixin, TimeMixin
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class Level(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "levels"
    __table_args__ = {"extend_existing": True}

    rating = Column(Integer)
    bpm = Column(Integer)
    notes = Column(Integer)
    length = Column(Integer)
    coverHash = Column(String(128))
    bgmHash = Column(String(128))
    dataHash = Column(String(128))
    engine_id = Column(Integer, ForeignKey("engines.id"))
    background_id = Column(Integer, ForeignKey("backgrounds.id"))
    effect_id = Column(Integer, ForeignKey("effects.id"))
    particle_id = Column(Integer, ForeignKey("particles.id"))
    skin_id = Column(Integer, ForeignKey("skins.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))
    pickup_id = Column(Integer, ForeignKey("pickups.id"))
    background = relationship("Background", back_populates="levels")
    engine = relationship("Engine", back_populates="levels")
    effect = relationship("Effect", back_populates="levels")
    particle = relationship("Particle", back_populates="levels")
    skin = relationship("Skin", back_populates="levels")
    genre = relationship("Genre", back_populates="levels")
    likes = relationship("Likes", back_populates="level")
    favorites = relationship("Favorites", back_populates="level")
