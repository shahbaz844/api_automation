import pytest
import requests
from assertpy import assert_that, soft_assertions
from requests.auth import HTTPBasicAuth

from api.api_client import Request
from api.endpoints import Endpoints
from tests.test_data.test_data import header, data

res = Request()

# pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4), (5, 7)])


@pytest.mark.usefixtures('getRequest')
class Tests:

    # @pytest.mark.usefixtures('getRequest')
    def test_get(self):
        payload = {'page': '2'}
        response = requests.get(Endpoints.BASE_URL + Endpoints.USERS, params=payload).json()
        with soft_assertions():
            assert_that(response['data'][0]['id']).is_equal_to(7)

    def test_post(self):
        a = getRequest
        print(a)
        url = Endpoints.BASE_URL + Endpoints.CREATE_USER
        response = Request.post_request(url, header, data)
        with soft_assertions():
            assert response['name'] == "morpheus", "Name response is not correct."
            assert_that(response['job']).is_equal_to("leader")

    def test_auth(self):
        basic = HTTPBasicAuth('user', 'pass')
        res = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
        print(res.json())
        assert res.status_code == 200


@pytest.mark.shah
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4), (5,6)])
def test_postt(n, expected):
    assert n + 1 == expected
