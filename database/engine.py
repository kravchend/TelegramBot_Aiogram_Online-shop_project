import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv

from database.models import Base

load_dotenv()

DATABASE_URL = os.getenv('DB_URL')

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не найдена в переменных окружения")

engine = create_async_engine(DATABASE_URL, echo=True)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
