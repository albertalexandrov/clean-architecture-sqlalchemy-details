from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import settings

engine = create_async_engine(settings.DB.async_dns, **settings.DB.OPTIONS)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)
metadata = MetaData()
