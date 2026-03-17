import pickle
from pathlib import Path

from pandas import DataFrame
from fastapi import APIRouter, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from helpers.url import analyze_url


router = APIRouter()

model0 = pickle.loads(Path("./machine_learning/model0.pkl").read_bytes())
model1 = pickle.loads(Path("./machine_learning/model1.pkl").read_bytes())
model2 = pickle.loads(Path("./machine_learning/model2.pkl").read_bytes())
model3 = pickle.loads(Path("./machine_learning/model3.pkl").read_bytes())


class RequestBody(BaseModel):
    robots_file: str | None = None
    har_file: str | None = None
    page_content: str | None = None
    url: str


class ResponseContent(BaseModel):
    robots_analyzed: bool
    har_analyzed: bool
    page_analyzed: bool
    url_analyzed: bool
    is_legit: bool


@router.post("/analyze")
def post(body: RequestBody):
    # Use model0.
    if (
        body.robots_file is not None
        and body.har_file is not None
        and body.page_content is not None
    ):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=ResponseContent(
                robots_analyzed=True,
                har_analyzed=True,
                page_analyzed=True,
                url_analyzed=True,
                is_legit=False,
            ).model_dump(),
        )

    # Use model1.
    if body.har_file is not None and body.page_content is not None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=ResponseContent(
                robots_analyzed=False,
                har_analyzed=True,
                page_analyzed=True,
                url_analyzed=True,
                is_legit=False,
            ).model_dump(),
        )

    # Use model2.
    if body.page_content is not None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=ResponseContent(
                robots_analyzed=False,
                har_analyzed=False,
                page_analyzed=True,
                url_analyzed=True,
                is_legit=False,
            ).model_dump(),
        )

    # Use model3.
    data = analyze_url(body.url)
    dataframe = DataFrame(data=data, columns=list(data.keys()))
    result = model3.predict(dataframe)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseContent(
            robots_analyzed=False,
            har_analyzed=False,
            page_analyzed=False,
            url_analyzed=True,
            is_legit=result[0],
        ).model_dump(),
    )
