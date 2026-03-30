from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.v1.analyze import router as analyze
from routes.v2.analyze import router as analyze2


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze)
app.include_router(analyze2)


@app.get("/")
def read_root():
    return HTMLResponse(content='Go to <a href="/docs">/docs</a>', status_code=200)
