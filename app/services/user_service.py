from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from .password_manager import PasswordManager
from ..database.models import User
from ..exceptions import username_already_taken_exception
from ..schemas import UserCreation, UserCreated


class UserService:
    @classmethod
    async def add_user(cls, session: AsyncSession, user: UserCreation) -> UserCreated:
        if await cls.get_user_by_username(session, user.username) is not None:
            raise username_already_taken_exception
        password = PasswordManager.get_random_password()
        new_user = User(username=user.username, password=PasswordManager.get_password_hash(password),
                        role=user.role)
        session.add(new_user)
        await session.commit()
        return UserCreated(username=user.username, password=password, role=user.role)

    @classmethod
    async def get_user_by_id(cls, session: AsyncSession, user_id: int) -> User | None:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @classmethod
    async def get_user_by_username(cls, session: AsyncSession, username: str) -> User | None:
        result = await session.execute(select(User).where(func.lower(User.username) == username.lower()))
        return result.scalar_one_or_none()
