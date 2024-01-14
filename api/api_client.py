import requests


class Request:

    @staticmethod
    def get_request(url):
        res = requests.get(url)
        return res.json()

    @staticmethod
    def post_request(url, header, data):
        res = requests.post(url, headers=header, json=data)
        return res.json()
