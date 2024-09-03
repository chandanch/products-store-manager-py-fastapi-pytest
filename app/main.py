from fastapi import FastAPI

import logging
import logging.config

app = FastAPI()

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@app.get("/healthcheck")
def health_check():
    logger.debug("Testing API Health")
    return {"status": "Server is Up & Running!"}
