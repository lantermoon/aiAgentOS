import os
import uvicorn
import webbrowser
from contextlib import asynccontextmanager
from threading import Timer

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import get_settings
from app.models.db import init_db
from app.controllers.auth import router as auth_router
from app.controllers.home import router as home_router

settings = get_settings()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_html(filename: str) -> str:
    path = os.path.join(BASE_DIR, "app", "views", filename)
    with open(path, encoding="utf-8") as f:
        return f.read()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
    )

    static_dir = os.path.join(BASE_DIR, "app", "static")
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router)
    app.include_router(home_router)

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "app": settings.APP_NAME, "version": settings.APP_VERSION}

    @app.get("/login", response_class=HTMLResponse)
    async def login_page():
        return read_html("login.html")

    @app.get("/index", response_class=HTMLResponse)
    async def index_page():
        return read_html("index.html")

    @app.get("/", response_class=HTMLResponse)
    async def root():
        return read_html("login.html")

    return app


app = create_app()

def _open_browser():
    webbrowser.open("http://localhost:8000/")


if __name__ == "__main__":
    if settings.DEBUG:
        Timer(1.5, _open_browser).start()
    uvicorn.run(
        "start_server:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )