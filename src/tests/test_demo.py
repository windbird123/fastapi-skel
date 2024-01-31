from fastapi.testclient import TestClient

from src.main import app
from src.modules import deps
from src.repo import Repo

client = TestClient(app)


class TestRepo(Repo):
    def server_id(self) -> str:
        return "test_server"


def test_demo():
    response = client.get("/api/v1/demo?name=windbird123")
    assert response.status_code == 200
    assert response.json() == {"message": "prod_server windbird123"}


def test_with_mock():
    with deps.override_for_test() as test_container:
        test_container[Repo] = TestRepo()
        response = client.get("/api/v1/demo?name=windbird123")

    assert response.status_code == 200
    # prod_server 대신에 test_server 가 리턴되어야 함
    assert response.json() == {"message": "test_server windbird123"}
