import pytest
from framework.db.db_utils import DbUtils
from framework.db.db_const import DB_NAME
import os

@pytest.fixture(scope='module')
def fix_from_db():
    db_obj = DbUtils(db_name=DB_NAME)
    db_obj.connect_for_db()
    db_obj.create_table()
    db_obj.add_user_in_table()
    return db_obj

@pytest.fixture(scope='module',autouse=True)
def fix_from_delete_db():
    yield
    os.remove(DB_NAME)
