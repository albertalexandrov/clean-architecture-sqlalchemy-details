from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model = None  # SQLAlchemy model

    def __init__(self, session: AsyncSession = Depends()):
        self._session = session

    async def get_by_pk(self, pk, options=()):
        return await self._session.get(self.model, pk, options=options)

    # another methods
