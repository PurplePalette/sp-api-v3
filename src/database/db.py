from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.database.config import ASYNC_DB_URL

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> sessionmaker:
    async with async_session() as session:
        yield session
