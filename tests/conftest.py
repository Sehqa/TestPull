import pytest
from framework.utils.custom_assert import CustomAssert
from framework.db.db_utils import ForDb



@pytest.fixture(scope='function',autouse=True)
def teardown():
    yield
    CustomAssert.show_error()
