from database.objects.favorite import Favorite
from database.objects.like import Like
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import func, relationship, select
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


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
    engineId = Column(Integer, ForeignKey("engines.id"))
    backgroundId = Column(Integer, ForeignKey("backgrounds.id"))
    effectId = Column(Integer, ForeignKey("effects.id"))
    particleId = Column(Integer, ForeignKey("particles.id"))
    skinId = Column(Integer, ForeignKey("skins.id"))
    genreId = Column(Integer, ForeignKey("genres.id"))
    background = relationship("Background", back_populates="levels", uselist=False)
    engine = relationship("Engine", back_populates="levels", uselist=False)
    effect = relationship("Effect", back_populates="levels", uselist=False)
    particle = relationship("Particle", back_populates="levels", uselist=False)
    skin = relationship("Skin", back_populates="levels", uselist=False)
    genre = relationship("Genre", back_populates="levels")
    likes = relationship("Like", back_populates="level")
    favorites = relationship("Favorite", back_populates="level")
    votes = relationship("Vote", back_populates="level")
    pickup = relationship("Pickup", back_populates="level", uselist=False)
    user = relationship("User", back_populates="levels", uselist=False)

    @hybrid_property
    def num_favorites(self) -> int:
        return self.favorites.count()  # type: ignore

    @num_favorites.expression
    def _num_favorites_expression(cls) -> select:
        return select([func.count(Favorite.id)]).where(Favorite.levelId == cls.id)

    @hybrid_property
    def num_likes(self) -> int:
        return len(self.likes)  # type: ignore

    @num_likes.expression
    def _num_likes_expression(cls) -> select:
        return select([func.count(Like.id)]).where(Like.levelId == cls.id)
