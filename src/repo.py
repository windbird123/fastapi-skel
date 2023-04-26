class Repo:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def show(self):
        print(f"{self.host=} {self.port=}")

    def hello(self):
        print(f"hello ${self.host}")
