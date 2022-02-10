import pytest
from .framework.http.for_get_post import GetPost
from .framework.utils.custom_assert import CustomAssert


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("answer_code", [200])
def test_get_request(url, headers, params, answer_code):
    CustomAssert.my_assert(GetPost.mock_get_http(url, params, headers) == answer_code)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("answer_code", [202])
def test2_get_request(url, headers, params, answer_code):
    CustomAssert.my_assert(GetPost.mock_get_http(url, params, headers) == answer_code)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("bodys", [{'key1': 'value1'}])
@pytest.mark.parametrize("answer_code", [200])
def test_post_request(url, headers, params, answer_code, bodys):
    CustomAssert.my_assert(GetPost.mock_post_http(url, params, headers, bodys) == answer_code)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("bodys", [{'key1': 'value1'}])
@pytest.mark.parametrize("answer_code", [202])
def test2_post_request(url, headers, params, answer_code, bodys):
    CustomAssert.my_assert(GetPost.mock_post_http(url, params, headers, bodys) == answer_code)
