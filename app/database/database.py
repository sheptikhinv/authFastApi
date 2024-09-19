from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        from ..database import User, Role
        from ..services import PasswordManager

        admin_user = await session.execute(
            select(User).where(User.username == "admin")
        )
        admin_user = admin_user.scalar_one_or_none()
        if not admin_user:
            password = PasswordManager.get_random_password()
            admin_user = User(username="admin", password=PasswordManager.get_password_hash(password), role=Role.ADMIN)
            print(f"Your admin credentials\nUsername: admin\nPassword: {password}")
            session.add(admin_user)
            await session.commit()
