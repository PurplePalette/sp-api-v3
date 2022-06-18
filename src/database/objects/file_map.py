from sqlalchemy import Column, Integer, String
from src.database.db import Base


class FileMap(Base):  # type: ignore
    __tablename__ = "file_maps"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    createdTime = Column(Integer, nullable=False)
    beforeType = Column(String(64), nullable=False)
    beforeHash = Column(String(256), nullable=False)
    afterType = Column(String(64), nullable=False)
    afterHash = Column(String(256), nullable=False)
    processType = Column(String(64), nullable=False)
