import uvicorn
from fastapi import FastAPI
from loguru import logger

from src.api import create_app
from src.config import settings

app: FastAPI = create_app()

# setup logger
logger.add(
    "logs/application.log",
    encoding="utf-8",
    rotation="00:00",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS}\t{level}\t{message}",
    level="INFO",
    retention="40 days",
    compression="zip",
    watch=True,
)

if __name__ == "__main__":
    logger.info(settings.logging.model_dump_json())
    logger.info(settings.database.model_dump_json())

    uvicorn.run(app, host="0.0.0.0", port=8080)
