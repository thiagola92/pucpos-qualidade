import json
from pathlib import Path

from pandas import DataFrame
from fastapi import APIRouter, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from utils import get_model
from machine_learning_remake.helper import analyze_url


router = APIRouter()
model = get_model(2)
tld_occurrence = json.loads(Path("./machine_learning_remake/tld.json").read_text())


class RequestBody(BaseModel):
    url: str


class ResponseContent(BaseModel):
    is_legit: bool


@router.post("/v2/analyze")
def post(body: RequestBody):
    data = analyze_url(body.url, tld_occurrence)

    for k in data:
        data[k] = [data[k]]

    dataframe = DataFrame(data=data, columns=list(data.keys()))
    result = model.predict(dataframe)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseContent(
            is_legit=result[0],
        ).model_dump(),
    )
