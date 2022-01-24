from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin
from src.database.objects import Level


class Pickup(Base, TimeMixin):  # type: ignore
    __tablename__ = "pickups"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    order = Column(Integer)
    level: Level = relationship("Level", backref="pickup", uselist=False)
