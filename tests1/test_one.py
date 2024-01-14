import pytest
import requests
from requests.auth import HTTPBasicAuth


def test_one():
    print('newwwww testttttt oneeeeeeeee')


# @pytest.mark.shah
def test_sess():
    r = requests.Session()
    basic = HTTPBasicAuth('user', 'pass')
    res = r.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
    print(f'session response status code {res.status_code}')
    print(f'session response {res.json()}')


@pytest.mark.shah
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
