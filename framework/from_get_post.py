import requests


class GetPost(object):
    @staticmethod
    def get_http(urls, paramss, headerss):
        req = requests.get(url=urls, params=paramss, headers=headerss)
        return req

        # метод для post

    @staticmethod
    def post_http(urls, paramss, headerss, bodys):
        req = requests.post(url=urls, params=paramss, headers=headerss, data=bodys)
        return req
