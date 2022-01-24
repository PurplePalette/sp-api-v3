from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin


class Like(Base, TimeMixin):  # type: ignore
    __tablename__ = "likes"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="likes", uselist=False)
    level_id = Column(Integer, ForeignKey("levels.id"))
    level = relationship("Level", back_populates="likes", uselist=False)
