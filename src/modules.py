from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration

from repo import Repo

container = Container()
container[Repo] = Repo(host='localhost', port=12345)

deps = FastApiIntegration(container)
