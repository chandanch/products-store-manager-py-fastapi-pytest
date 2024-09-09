from fastapi import FastAPI

import logging
import logging.config
from app.routers.category import category_router

app = FastAPI()
app.include_router(category_router, prefix="/api/category", tags=["category"])


logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@app.get("/healthcheck", tags=["healthcheck"])
def health_check():
    logger.debug("Testing API Health")
    return {"status": "Server is Up & Running!"}
