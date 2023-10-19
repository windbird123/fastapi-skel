import uvicorn

from src.api import create_app
from src.config import settings

app = create_app()

if __name__ == "__main__":
    print(settings.logging.model_dump_json())
    print(settings.database.model_dump_json())

    uvicorn.run(app, host="0.0.0.0", port=8080)
