from framework.utils import Utils
from smart_assertions import soft_assert, verify_expectations
from framework.listmet import ListMet
from framework.db import Db
import pytest

@pytest.fixture(scope='module')
def teardowns():
    verify_expectations()
