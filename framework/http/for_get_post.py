import requests
import requests_mock
from framework.utils.http_logger import HttpLogger


class GetPost(object):
    @staticmethod
    @HttpLogger.logger(level=3, message='LogMessage',filename='log_one.txt')
    def get_http(urls, paramss, headerss):
        req = requests.get(url=urls, params=paramss, headers=headerss)
        return req

    @staticmethod
    def mock_get_http(url, headers, params):
        with requests_mock.Mocker() as moc:
            moc.get(url=url, status_code=200)
            req = GetPost.get_http(url, params, headers)
        return req.status_code

    @staticmethod
    @HttpLogger.logger(level=2, message=None,filename='log_two.txt')
    def post_http(urls, paramss, headerss, bodys):
        req = requests.post(url=urls, params=paramss, headers=headerss, data=bodys)
        return req

    @staticmethod
    def mock_post_http(url, headers, params, bodys):
        with requests_mock.Mocker() as moc:
            moc.post(url=url, status_code=200)
            req = GetPost.post_http(url, headers, params, bodys)
        return req.status_code
