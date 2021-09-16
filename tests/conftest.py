import pytest
from framework.utils.custom_assert import CustomAssert
from framework.db.db_utils import ForDb


@pytest.fixture(scope='module',autouse=True)
def teardown():
    yield
    CustomAssert.show_error()


@pytest.fixture(scope='module')
def fix_from_db():
    with open('../framework/db/database_name.txt','r') as inf:
        db_names=inf.read()
    db_obj = ForDb(db_name=db_names)
    db_obj.connect_for_db()
    db_obj.create_table()
    db_obj.add_user_in_table()
    return db_obj