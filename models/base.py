from sqlalchemy.orm import DeclarativeBase

from db import metadata


class Base(DeclarativeBase):
    metadata = metadata
