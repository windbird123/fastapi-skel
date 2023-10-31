from pathlib import Path

from loguru import logger
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_PATH = Path(__file__).parent.parent.parent
logger.info(f"{ROOT_PATH=}")


class DatabaseSettings(BaseModel):
    name: str = "db.sqlite3"

    @property
    def url(self) -> str:
        return f"sqlite+aiosqlite:///./{self.name}"


class LoggingSettings(BaseModel):
    file: str = "CHANGEME"
    rotation_size: str = "10MB"
    compression: str = "zip"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__", env_file=".env", extra="ignore", case_sensitive=False
    )

    root_dir: Path
    src_dir: Path

    database: DatabaseSettings = DatabaseSettings()
    logging: LoggingSettings = LoggingSettings()


# NOTE: We would like to hard-code the root and applications directories
#       to avoid overriding via environment variables
settings = Settings(
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "src",
)
