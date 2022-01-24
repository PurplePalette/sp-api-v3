from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Level(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "levels"
    __table_args__ = {"extend_existing": True}

    rating = Column(Integer)
    bpm = Column(Integer)
    notes = Column(Integer)
    length = Column(Integer)
    cover_hash = Column(String(128))
    bgm_hash = Column(String(128))
    data_hash = Column(String(128))
    engine_id = Column(Integer, ForeignKey("engines.id"))
    background_id = Column(Integer, ForeignKey("backgrounds.id"))
    effect_id = Column(Integer, ForeignKey("effects.id"))
    particle_id = Column(Integer, ForeignKey("particles.id"))
    skin_id = Column(Integer, ForeignKey("skins.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))
    background = relationship("Background", back_populates="levels", uselist=False)
    engine = relationship("Engine", back_populates="levels", uselist=False)
    effect = relationship("Effect", back_populates="levels", uselist=False)
    particle = relationship("Particle", back_populates="levels", uselist=False)
    skin = relationship("Skin", back_populates="levels", uselist=False)
    genre = relationship("Genre", back_populates="levels")
    likes = relationship("Like", back_populates="level")
    favorites = relationship("Favorite", back_populates="level")
    pickup = relationship("Pickup", back_populates="level", uselist=False)
    user = relationship("User", back_populates="levels", uselist=False)
