import pytest
from framework.db.db_utils import ForDb
from framework.db.db_const import DB_NAME


@pytest.fixture(scope='module')
def fix_from_db():
    db_obj = ForDb(db_name=DB_NAME)
    db_obj.connect_for_db()
    db_obj.create_table()
    db_obj.add_user_in_table()
    return db_obj
