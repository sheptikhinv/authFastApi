from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from ..exceptions import auth_exception
from ..schemas import UserLogin, Token
from ..services import TokenManager, PasswordManager, UserService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
async def login(user: UserLogin, session: AsyncSession = Depends(get_session)):
    user_db = await UserService.get_user_by_username(session=session, username=user.username)
    if user_db is None or not PasswordManager.verify_password(plain_password=user.password,
                                                              hashed_password=user_db.password):
        raise auth_exception
    return Token(access_token=TokenManager.create_token(data={"sub": str(user_db.id)}), token_type="Bearer")
