from pydantic import BaseModel, Field, validator

from src.config import settings
from src.utils.storage import CACHE


class Build(BaseModel):
    name: str = Field(..., alias="build_name")

    @validator("name", pre=True)
    def existing_name(cls, value: str) -> str:
        if value not in CACHE["builds"]:
            raise ValueError(
                f"Build {value} not found "
                f"in '{settings.builds_file_path}' file"
            )
        return value

    async def get_tasks(self) -> list[str]:
        sorted_tasks = []
        visited = set()

        def visit(task_name: str) -> None:
            if task_name in visited:
                return
            visited.add(task_name)
            task = CACHE["tasks"].get(task_name)
            if task is None:
                raise ValueError(
                    f"Task {task_name} not found "
                    f"in '{settings.tasks_file_path}' file"
                )

            for dependency in task:
                visit(dependency)
            sorted_tasks.append(task_name)

        for task_name in CACHE["builds"][self.name]:
            visit(task_name)

        return sorted_tasks
