import pytest
import requests
from requests.auth import HTTPBasicAuth


class Sessions:

    @pytest.mark.shah
    def test_sess(self):
        r = requests.Session()
        basic = HTTPBasicAuth('user', 'pass')
        res = r.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
        print(f'session response status code {res.status_code}')
        print(f'session response {res.json()}')
