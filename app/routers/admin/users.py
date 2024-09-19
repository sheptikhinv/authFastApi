from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...database import get_session
from ...schemas import UserCreation, UserCreated
from ...services import UserService

router = APIRouter(prefix="/users", tags=["Users management"])


@router.post("/create", response_model=UserCreated)
async def create_user(user: UserCreation, session: AsyncSession = Depends(get_session)):
    return await UserService.add_user(session, user)
