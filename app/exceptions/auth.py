from fastapi import HTTPException
from starlette import status

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

auth_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid username or password"
)

permissions_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You do not have permission to perform this operation."
)
