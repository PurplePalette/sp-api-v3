from db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Genre(Base):  # type: ignore
    __tablename__ = "genres"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    name_en = Column(String(128))
    levels = relationship("Level", back_populates="genre")
