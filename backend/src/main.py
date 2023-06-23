import time
import asyncio

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from .auth.kc import KeycloakService
from .config import settings

app = FastAPI(
    title="CubeOn back",
    openapi_url='/docs/openapo.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)


@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    print(
        f"Метод: {request.method}, Путь: {request.url.path}, Время выполнения: {end_time - start_time} сек.")

    return response


@app.post('/auth')
async def authorize(username: str, password: str, s: KeycloakService = Depends()):
    res = await s.auth(username, password)
    return res


@app.get("/", response_class=HTMLResponse)
async def home():

    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """
