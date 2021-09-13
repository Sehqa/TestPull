from smart_assertions import verify_expectations
import pytest

@pytest.fixture(scope='module')
def teardowns():
    verify_expectations()
