from db import Base
from mixins import TimeMixin
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Like(Base, TimeMixin):  # type: ignore
    __tablename__ = "likes"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="likes")
    level_id = Column(Integer, ForeignKey("levels.id"))
    level = relationship("Level", backref="likes")
