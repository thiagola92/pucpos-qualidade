from pandas import DataFrame
from fastapi import APIRouter, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from utils import get_model
from machine_learning.helper import analyze_url


router = APIRouter()
model = get_model(1)


class RequestBody(BaseModel):
    url: str


class ResponseContent(BaseModel):
    is_legit: bool


@router.post("/v1/analyze")
def post(body: RequestBody):
    data = analyze_url(body.url)
    dataframe = DataFrame(data=data, columns=list(data.keys()))
    result = model.predict(dataframe)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseContent(
            is_legit=result[0],
        ).model_dump(),
    )
