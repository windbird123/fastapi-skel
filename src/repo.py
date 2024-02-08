from abc import ABC, abstractmethod

from loguru import logger


class Repo(ABC):
    @abstractmethod
    def server_id(self) -> str:
        raise NotImplementedError


class ProdRepo(Repo):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def server_id(self) -> str:
        logger.info(f"server {self.host}:{self.port}")
        return "prod_server"
