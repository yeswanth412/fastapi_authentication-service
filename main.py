from fastapi import FastAPI

from app.core.config import APP_NAME, APP_VERSION
from app.routes.auth import router as auth_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(auth_router, tags=["Authentication"])

@app.get("/")
async def home():
    return {
        "message": "Authentication Service Running"
    }