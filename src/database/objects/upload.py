from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin


class Upload(Base, TimeMixin):  # type: ignore
    __tablename__ = "uploads"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="uploads", uselist=False)
    # LevelCover, LevelBgm...
    objectType = Column(String(64))
    # Size in bytes
    objectSize = Column(Integer)
    # SHA1 Hash
    objectHash = Column(String(256))
    # Original filename
    objectName = Column(String(256))
    # level/engine/background (table name)
    objectTargetType = Column(String(32), nullable=True)
    # levelId/engineId/backgroundId
    objectTargetId = Column(Integer, nullable=True)
