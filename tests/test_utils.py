from framework.lists.for_list import ListMet
from framework.db.db_utils import ForDb
from framework.utils.custom_assert import CustomAssert

import pytest


@pytest.mark.parametrize("list1", [(1, 2, 3)])
@pytest.mark.parametrize("list2", [(1, 2, 3)])
@pytest.mark.parametrize("type_in_obj", ['str'])
def test_mas(list1, list2, type_in_obj):
    list_compars_obj = ListMet()
    CustomAssert.my_assert(list_compars_obj.compars_mass(list1, list2, type_in_obj))


@pytest.mark.parametrize("list1", [('345')])
@pytest.mark.parametrize("list2", [('ddddd')])
@pytest.mark.parametrize("type_in_obj", ['ssaasdrw,fsdfsd,fdsfsd,111111111'])
# negative
def test2_mas(list1, list2, type_in_obj):
    list_compars_obj = ListMet()
    CustomAssert.my_assert(list_compars_obj.compars_mass(list1, list2, type_in_obj))


@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('db_name', ["database1.db"])
@pytest.mark.parametrize('expected_dict',
                         [[{'userid': [22]}, {'fname': ['Alex4']}, {'lname': ['Smith4']}, {'gender': ['male4']}]])
def test_sqldict(request_for_db, db_name, expected_dict):
    obj_for_test = ForDb()
    obj_for_test.db_name = db_name
    obj_for_test.connect_for_db()
    CustomAssert.my_assert(obj_for_test.dict_from_db(request_for_db) == expected_dict)


@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('db_name', ["database1.db"])
@pytest.mark.parametrize('expected_dict',
                         [[{'userid': [22]}, {'fname': ['ATlex4']}, {'ss': ['Sss']}, {'gender': ['male4']}]])
def test2_sqldict(request_for_db, db_name, expected_dict):
    obj_for_test = ForDb()
    obj_for_test.db_name = db_name
    obj_for_test.connect_for_db()
    CustomAssert.my_assert((obj_for_test.dict_from_db(request_for_db) == expected_dict))
