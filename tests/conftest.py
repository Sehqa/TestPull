import pytest
from framework.utils.custom_assert import CustomAssert

@pytest.fixture(scope='function',autouse=True)
def teardown():
    yield
    CustomAssert.show_error()
