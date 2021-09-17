from framework.lists.for_list import ListUtils
from framework.utils.waiting_method import Utils
from framework.utils.custom_assert import CustomAssert
import pytest


@pytest.mark.parametrize("list1,list2,type_in_obj", [([1, 2, 3], [1, 2, 3], 'str')])
def test_mas(list1, list2, type_in_obj):
    list_compars_obj = ListUtils()
    CustomAssert.my_assert(list_compars_obj.compars_mass(list1, list2, type_in_obj))


@pytest.mark.parametrize("list1", [([1, 2, 3])])
@pytest.mark.parametrize("list2", [([1, 2, 4])])
@pytest.mark.parametrize("type_in_obj", ['int'])
def test2_mas(list1, list2, type_in_obj):
    list_compars_obj = ListUtils()
    CustomAssert.my_assert(list_compars_obj.compars_mass(list1, list2, type_in_obj))


@pytest.mark.parametrize("timeout", [20])
@pytest.mark.parametrize("period", [5])
@pytest.mark.parametrize("arg", [5])
def test_waiting(timeout, period, arg):
    CustomAssert.my_assert(Utils.wait_for_result(Utils.add_in_result_list, timeout, period, arg) == True)


@pytest.mark.parametrize("timeout", [5])
@pytest.mark.parametrize("period", [5])
@pytest.mark.parametrize("arg", [5])
def test2_waiting(timeout, period, arg):
    CustomAssert.my_assert(Utils.wait_for_result(Utils.add_in_result_list, timeout, period, arg) == True)


@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('expected_dict',
                         [[{'userid': [22]}, {'fname': ['Alex4']}, {'lname': ['Smith4']}, {'gender': ['male4']}]])
def test_sqldict(request_for_db, expected_dict, fix_from_db):
    CustomAssert.my_assert (fix_from_db.return_dictionary_list(request_for_db) == expected_dict)


@pytest.mark.parametrize('request_for_db', ["SELECT * FROM users;"])
@pytest.mark.parametrize('expected_dict',
                         [[{'userid': [22]}, {'fname': ['ATlex4']}, {'ss': ['Sss']}, {'gender': ['male4']}]])
def test2_sqldict(request_for_db, fix_from_db, expected_dict):
    CustomAssert.my_assert(fix_from_db.return_dictionary_list(request_for_db) == expected_dict)
