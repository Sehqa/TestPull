from smart_assertions import soft_assert, verify_expectations
from framework.lists.for_list import ListMet
from framework.db.db_utils import ForDb
import pytest

def teardown():
    verify_expectations()


@pytest.mark.parametrize("list1", [(1, 2, 3)])
@pytest.mark.parametrize("list2", [(1, 2, 3)])
@pytest.mark.parametrize("typeinobj", ['str'])
def test_mas(list1, list2, typeinobj):
    listcomparsobj = ListMet()
    soft_assert(listcomparsobj.compars_mass(list1, list2, typeinobj))


@pytest.mark.parametrize("list1", [('bool')])
@pytest.mark.parametrize("list2", [('ddddd')])
@pytest.mark.parametrize("typeinobj", ['ssaasdrw,fsdfsd,fdsfsd,111111111'])
# negative
def test2_mas(list1, list2, typeinobj):
    soft_assert(ListMet.compars_mass(list1, list2, typeinobj))





@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('db_name', ["database1.db"])
def test_sqldict(request_for_db,db_name):
    Databas=ForDb()
    Databas.db_name=db_name
    assert (Databas.dict_from_db(request_for_db))


@pytest.mark.parametrize('request_for_db', ['ssssss'])
# negative
def test2_sqldict(request_for_db):
    Databas = ForDb()
    assert (Databas.dict_from_db(request_for_db))


