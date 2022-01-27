from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base


class Genre(Base):  # type: ignore
    __tablename__ = "genres"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    nameEn = Column(String(128))
    levels = relationship("Level", back_populates="genre")
