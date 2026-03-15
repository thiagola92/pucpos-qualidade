from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from routes.analyze import router as analyze


app = FastAPI()

app.include_router(analyze)


@app.get("/")
def read_root():
    return HTMLResponse(content='Go to <a href="/docs">/docs</a>', status_code=200)
