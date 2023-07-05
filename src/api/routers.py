from fastapi import APIRouter

from src.api.endpoints import tasks

api_router = APIRouter(prefix="/api")

api_router.include_router(tasks.router, prefix="/tasks")
