from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse

from modules import deps
from repo import Repo

router = APIRouter(prefix='/api/v1')


class Result(BaseModel):
    message: str


class Error(BaseModel):
    code: int


# https://fastapi.tiangolo.com/advanced/additional-responses/ 참고
@router.get('/demo', response_model=Result, responses={400: {"model": Error}})
def demo(name: str, repo: Repo = deps.depends(Repo)):
    repo.show()
    if name == 'error':
        error = Error(code=400)
        return JSONResponse(content=jsonable_encoder(error), status_code=400)
    return Result(message=f'hello {name}')
