from typing import List, Annotated

from fastapi import Depends

from . import TokenManager
from ..database import Role, User
from ..exceptions import permissions_exception


class RoleChecker:
    def __init__(self, allowed_roles: List[Role]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[User, Depends(TokenManager.get_current_user)]):
        if user.role in self.allowed_roles or user.role == Role.ADMIN:
            return True
        raise permissions_exception
