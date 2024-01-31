import uvicorn
from fastapi import FastAPI
from loguru import logger

from src.api import create_app
from src.config import settings

app: FastAPI = create_app()

if __name__ == "__main__":
    logger.add("file_{time}.log",
        encoding="utf-8",
               rotation="18:45", 
               format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}", 
               level="INFO", 
               retention="40 days", 
               compression="zip",
               watch=True)

    logger.info(settings.logging.model_dump_json())
    logger.info(settings.database.model_dump_json())

    uvicorn.run(app, host="0.0.0.0", port=8080)
