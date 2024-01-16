from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.limiter import limiter
from src.modules import deps
from src.repo import Repo

router = APIRouter(prefix="/api/v1")


class Result(BaseModel):
    message: str


class Error(BaseModel):
    code: int


# https://fastapi.tiangolo.com/advanced/additional-responses/ 참고
# limiter.limit 사용을 위해서는 request param 이 필요함
@router.get("/demo", response_model=Result, responses={400: {"model": Error}})
@limiter.limit("2/minute")
async def demo(request: Request, name: str, repo: Repo = deps.depends(Repo)):
    if name == "error":
        error = Error(code=400)
        return JSONResponse(content=jsonable_encoder(error), status_code=400)
    return Result(message=f"{repo.server_id()} {name}")
