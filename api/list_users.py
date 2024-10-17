from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app import app
from models.users import User
from repositories.users import UsersRepository


class Schema(BaseModel):
    class ProfileSchema(BaseModel):
        id: int
        age: int
        hobby: str
        address: str

    id: int
    first_name: str
    last_name: str
    username: str


class Repository:
    """This endpoint repository that incapsulates getting user with options.
    I had to create it because I had to use selectinload that is a detail of data layer (of SQLAlchemy)
    and according to clean architecture service should not know about it
    """

    def __init__(self, session: AsyncSession = Depends()):
        self._session = session
        self._users_repository = UsersRepository(session)

    async def get_user(self, user_id: int):
        options = [selectinload(User.profile)]
        return await self._users_repository.get_by_pk(user_id, options)


class Service:
    """This endpoint service for demo purposes. It can be much more complex"""

    def __init__(self, repository: Repository = Depends()):
        self._repository = repository

    async def get_user(self, user_id: int):
        # some logic
        user = await self._repository.get_user(user_id)
        # some logic
        return user

    # another methods


@app.get("/user/{user_id}", response_model=Schema)
async def get_user(user_id: int, service: Service = Depends()):
    return await service.get_user(user_id)
