from fastapi import FastAPI

import demo
from modules import container
from repo import Repo

app = FastAPI()

app.include_router(demo.router)


@app.on_event("startup")
def startup():
    repo = container[Repo]
    repo.show()
