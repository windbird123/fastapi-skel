from fastapi import FastAPI

import demo
from modules import container
from repo import Repo

app = FastAPI()

app.include_router(demo.router)


# https://fastapi.tiangolo.com/advanced/events/
@app.on_event("startup")
def startup():
    repo = container[Repo]
    repo.show()


def shutdown_handler():
    print('server is shutdown')


app.on_event('shutdown')(shutdown_handler)
