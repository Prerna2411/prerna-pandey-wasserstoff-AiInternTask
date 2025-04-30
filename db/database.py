# backend/db/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

import os

# Load DB URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/game")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependency for FastAPI
async def get_db():
    async with async_session() as session:
        yield session

# Function to create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


