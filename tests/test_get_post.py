from smart_assertions import verify_expectations
import pytest
from framework.http.for_get_post import GetPost
from framework.utils.custom_assert import CustomAssert


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("answercode", [200])
def test_get_request(url,headers,params,answercode):
    CustomAssert.my_assert(GetPost.mock_get_http(url,params,headers)==answercode)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("answercode", [202])
def test2_get_request(url,headers,params,answercode):
    CustomAssert.my_assert (GetPost.mock_get_http(url,params,headers)==answercode)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("bodys", [{'key1': 'value1'}])
@pytest.mark.parametrize("answercode", [200])
def test_post_request(url,headers,params,answercode,bodys):
    CustomAssert.my_assert (GetPost.mock_post_http(url, params, headers,bodys) == answercode)


@pytest.mark.parametrize("url", ['http://example.com/get_status'])
@pytest.mark.parametrize("headers", [{'accept': '*/*'}])
@pytest.mark.parametrize("params", [{'key1': 'value1'}])
@pytest.mark.parametrize("bodys", [{'key1': 'value1'}])
@pytest.mark.parametrize("answercode", [202])
def test2_post_request(url,headers,params,answercode,bodys):
    CustomAssert.my_assert (GetPost.mock_post_http(url, params, headers,bodys) == answercode)

