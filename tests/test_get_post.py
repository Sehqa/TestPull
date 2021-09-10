from smart_assertions import soft_assert, verify_expectations
import requests_mock
from framework.from_get_post import GetPost


def teardown():
    verify_expectations()


def test_get_request():
    with requests_mock.Mocker() as moc:
        moc.get(url='http://example.com/get_status', status_code=200)
        req = GetPost.get_http('http://example.com/get_status', {'accept': '*/*'}, \
                              {'key1': 'value1'})
        soft_assert(req.status_code == 200)

def test2_get_request():
    with requests_mock.Mocker() as moc:
        moc.get(url='http://example.com/get_status', status_code=404)
        req = GetPost.get_http('http://example.com/get_status', \
                              {'accept': '*/*'}, {'key1': 'value1'})
        soft_assert(req.status_code == 200)



def test_post_request():
    with requests_mock.Mocker() as moc:
        moc.post(url='http://example.com/get_status', status_code=404)
        req = GetPost.post_http('http://example.com/get_status', \
                               {'accept': '*/*'}, {'key1': 'value1'}, {'key1': 'value1'})
        soft_assert(req.status_code == 404)

#negative
def test2_post_request():
    with requests_mock.Mocker() as moc:
        moc.post(url='http://example.com/get_status', status_code=400)
        req = GetPost.post_http('http://example.com/get_status', {'  '}, {' '}, {'gg'})
        soft_assert(req.status_code == 400)