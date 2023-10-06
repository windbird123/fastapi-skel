from fastapi import FastAPI

import src.demo
from src.modules import container
from src.repo import Repo


def startup():
    repo = container[Repo]
    repo.show()


def shutdown_handler():
    print('server is shutdown')


def create_app():
    app = FastAPI()

    # https://fastapi.tiangolo.com/advanced/events/
    app.on_event("startup")(startup)
    app.on_event("shutdown")(shutdown_handler)

    app.include_router(src.demo.router)
    return app
