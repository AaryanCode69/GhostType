from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL,echo = True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit = False,
    autoflush = False,
    expire_on_commit = False
)

class Base(AsyncAttrs,DeclarativeBase):
    pass