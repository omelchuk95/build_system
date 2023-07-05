from functools import lru_cache

from pydantic import BaseSettings, FilePath


class Settings(BaseSettings):
    tasks_file_path: FilePath = "builds/tasks.yaml"
    builds_file_path: FilePath = "builds/builds.yaml"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
