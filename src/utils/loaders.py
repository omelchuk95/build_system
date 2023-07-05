import yaml

from src.config import settings


async def load_tasks() -> dict:
    tasks = {}

    with open(settings.tasks_file_path, "r") as file:
        tasks_data = yaml.safe_load(file)
        for task in tasks_data["tasks"]:
            tasks[task["name"]] = task["dependencies"]
    return tasks


async def load_builds() -> dict:
    builds = {}

    with open(settings.builds_file_path, "r") as file:
        builds_data = yaml.safe_load(file)
        for build in builds_data["builds"]:
            builds[build["name"]] = build["tasks"]
    return builds
