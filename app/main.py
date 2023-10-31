import os

import uvicorn
from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.constants import constants
from app.utils import logger

logger = logger.get_logger(logger_name="Fujin")

app = FastAPI(
    title=constants.TITLE,
    description="Fujin Backend Service",
    version=constants.VERSION,
    redoc_url=None,
    debug=True
)

app.include_router(
    router=api_router
    , prefix='/v1'
)


@app.get("/health")
async def check_health() -> dict:
    return {'status': 'OK'}


if __name__ == "main":
    logger.info("Start Server")

    API_HOST_PORT = int(os.getenv("SERVICE_PORT", 8000))
    API_HOST_DOMAIN = os.getenv("SERVICE_HOST", "0.0.0.0")
    NUMBER_OF_WORKER = os.getenv("WEB_CONCURRENCY", 1)
    RELOAD_CODE = False
    try:
        uvicorn.run(
            "app.main:app",
            host=API_HOST_DOMAIN,
            port=API_HOST_PORT,
            reload=RELOAD_CODE,
            workers=NUMBER_OF_WORKER
        )

    except SystemExit:
        logger.error("Failed to start the server.")
        raise
