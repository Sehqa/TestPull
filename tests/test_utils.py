from framework.utils import Utils
from smart_assertions import soft_assert, verify_expectations
from framework.listmet import ListMet
from framework.db import Db
import requests
from framework.utils import Utils
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
    soft_assert(ListMet._compars_mass(list1, list2, typeinobj))





@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('db_name', ["database1.db"])
def test_sqldict(request_for_db,db_name):
    Databas=Db()
    Databas.db_name=db_name
    assert (Databas.dictfrombd(request_for_db))


@pytest.mark.parametrize('request_for_db', ['ssssss'])
# negative
def test2_sqldict(request_for_db):
    Databas = Db()
    assert (Databas.dictfrombd(request_for_db))


