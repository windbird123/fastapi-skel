from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

import src.demo
from src.modules import container
from src.repo import Repo


@asynccontextmanager
async def lifespan(app: FastAPI):
    repo = container[Repo]
    logger.info(f"Starts server, {repo.server_id()}")
    yield
    logger.info("Stop server ...")


def create_app() -> FastAPI:
    # https://fastapi.tiangolo.com/advanced/events/#lifespan-events
    app = FastAPI(lifespan=lifespan)

    app.include_router(src.demo.router)
    return app
