import pytest
import requests

from api.endpoints import Endpoints


@pytest.fixture(scope='package')
def getRequest():
    payload = {'page': '2'}
    response = requests.get(Endpoints.BASE_URL + Endpoints.USERS, params=payload).json()
    print(f'\nfixtturre response is correct\n')
    yield f'\nyielded responseeeee\n'
    print('clllooooosedddd.....')
