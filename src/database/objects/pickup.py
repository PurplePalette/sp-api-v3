from db import Base
from mixins import TimeMixin
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship


class Pickup(Base, TimeMixin):  # type: ignore
    __tablename__ = "pickups"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    order = Column(Integer)
    level = relationship("Level", backref="pickup", uselist=False)
