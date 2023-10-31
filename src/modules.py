from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration

from src.repo import ProdRepo, Repo

container = Container()
container[Repo] = ProdRepo(host="localhost", port=12345)

deps = FastApiIntegration(container)
