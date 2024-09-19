import asyncio

import uvicorn

from .database import init_db


def start_server():
    asyncio.run(init_db())
    uvicorn.run("app.routers.main:app")
