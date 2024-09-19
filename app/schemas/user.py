from pydantic import BaseModel

from ..database import Role


class UserBase(BaseModel):
    username: str


class UserLogin(UserBase):
    password: str


class UserCreation(UserBase):
    role: Role


class UserCreated(UserCreation):
    password: str


class User(UserBase):
    id: int
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
