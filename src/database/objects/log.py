from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin


class Log(Base, TimeMixin):  # type: ignore
    __tablename__ = "logs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="logs", uselist=False)
    type = Column(Integer)
    param1 = Column(String)
    param2 = Column(String)
    param3 = Column(String)
    raw = Column(String)
