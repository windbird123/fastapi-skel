from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

import src.demo
from src.limiter import limiter
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
    app: FastAPI = FastAPI(lifespan=lifespan)

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    app.include_router(src.demo.router)
    return app
