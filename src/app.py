import logging

from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

from src.api.routers import api_router
from src.utils.loaders import load_builds, load_tasks
from src.utils.storage import CACHE

app = FastAPI()

app.include_router(api_router)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    CACHE["tasks"] = await load_tasks()
    CACHE["builds"] = await load_builds()


@app.middleware("http")
async def catch_exceptions(request, call_next):
    try:
        response = await call_next(request)
    except HTTPException as http_exception:
        response = http_exception
    except Exception as exception:
        logger.error(
            f"An error occurred during "
            f"request processing. "
            f"Exception repr: {repr(exception)}"
        )

        response = JSONResponse(
            status_code=500,
            content={
                "detail": [
                    {
                        "msg": "Something went wrong... See logs for details.",
                    }
                ]
            },
        )
    return response
