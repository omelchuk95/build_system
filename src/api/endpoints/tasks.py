from fastapi import APIRouter

from src.api.schemas.build import Build

router = APIRouter()


@router.post("/", description="List of tasks for current build")
async def tasks(build_obj: Build) -> list[str]:
    return await build_obj.get_tasks()
