import uvicorn
from loguru import logger

from src.api import create_app
from src.config import settings

app = create_app()

if __name__ == "__main__":
    logger.info(settings.logging.model_dump_json())
    logger.info(settings.database.model_dump_json())

    uvicorn.run(app, host="0.0.0.0", port=8080)
