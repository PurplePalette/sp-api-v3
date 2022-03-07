from typing import List

from sqlalchemy import Boolean, Column, Integer, String, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin
from src.database.objects.favorite import Favorite
from src.database.objects.like import Like
from src.database.objects.log import Log
from src.database.objects.vote import Vote  # noqa: F401
from src.models.user import User as UserReqResp
from src.models.user_total import UserTotal
from src.models.user_total_publish import UserTotalPublish


class User(Base, TimeMixin):  # type: ignore
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(128), unique=True)
    testId = Column(String(128), unique=True)
    accountId = Column(String(128), unique=True)
    description = Column(String(512), default="", server_default="")
    isAdmin = Column(Boolean, default=False, server_default="0")
    isDeleted = Column(Boolean, default=False, server_default="0")
    backgrounds = relationship("Background", back_populates="user")
    effects = relationship("Effect", back_populates="user")
    engines = relationship("Engine", back_populates="user")
    levels = relationship("Level", back_populates="user")
    particles = relationship("Particle", back_populates="user")
    skins = relationship("Skin", back_populates="user")
    likes = relationship("Like", back_populates="user")
    favorites = relationship("Favorite", back_populates="user")
    announces = relationship("Announce", back_populates="user")
    votes = relationship("Vote", back_populates="user")
    logs = relationship("Log", back_populates="user")
    uploads = relationship("Upload", back_populates="user")

    def toItem(self) -> UserReqResp:
        return UserReqResp(
            userId=self.userId,
            testId=self.testId,
            accountId=self.accountId,
            description=self.description,
            createdTime=self.createdTime,
            updatedTime=self.updatedTime,
            total=UserTotal(
                likes=0,
                plays=0,
                favorites=0,
                publish=UserTotalPublish(
                    backgrounds=0,
                    effects=0,
                    engines=0,
                    particles=0,
                    levels=0,
                    skins=0,
                ),
            ),
            isAdmin=self.isAdmin,
            isDeleted=self.isDeleted,
        )

    @hybrid_property
    def ids_favorites(self) -> List[int]:
        return self.favorites  # type: ignore

    @ids_favorites.expression
    def _ids_favorites_expression(cls) -> select:
        return select([Favorite.id]).where(Favorite.userId == cls.id)

    @hybrid_property
    def ids_likes(self) -> List[int]:
        return self.likes  # type: ignore

    @ids_likes.expression
    def _ids_likes_expression(cls) -> select:
        return select([Like.id]).where(Like.userId == cls.id)

    @hybrid_property
    def ids_played(self) -> List[int]:
        return self.logs  # type: ignore

    @ids_played.expression
    def _ids_played_expression(cls) -> select:
        return select([Log.id]).where(Log.userId == cls.id, Log.type == 0)
