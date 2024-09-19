from fastapi import FastAPI

from .auth import router as auth_router
from .admin import admin_router

app = FastAPI()

app.include_router(admin_router)
app.include_router(auth_router)
