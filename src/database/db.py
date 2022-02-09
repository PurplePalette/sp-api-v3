from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from src.database.config import ASYNC_DB_URL, DB_URL

# 普通のリクエストで使う 非同期エンジン
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

# SEEDやTESTでのみ使う 同期エンジン
engine = create_engine(DB_URL, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)

Base = declarative_base()


async def get_db() -> sessionmaker:
    async with async_session() as session:
        yield session


def get_sync_db() -> sessionmaker:
    return scoped_session(session)
