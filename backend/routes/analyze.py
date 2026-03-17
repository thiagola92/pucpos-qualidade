import pickle
from pathlib import Path

from pandas import DataFrame
from fastapi import APIRouter, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from machine_learning.helper import analyze_url


router = APIRouter()
model = pickle.loads(Path("./machine_learning/model.pkl").read_bytes())


class RequestBody(BaseModel):
    url: str


class ResponseContent(BaseModel):
    is_legit: bool


@router.post("/analyze")
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
