from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin
from src.database.objects import Level  # noqa: F401


class Pickup(Base, TimeMixin):  # type: ignore
    __tablename__ = "pickups"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    order = Column(Integer)
    levelId = Column(Integer, ForeignKey("levels.id"))
    level = relationship("Level", back_populates="pickup", uselist=False)
