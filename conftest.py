import os
from requests import Session
from pytest import fixture


class BaseSession(Session):

    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = self.base_url + url
        return super().request(method, url, *args, **kwargs)


@fixture(scope='session')
def session():
    base_url = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')
    session = BaseSession(base_url)

    yield session

    session.close()
