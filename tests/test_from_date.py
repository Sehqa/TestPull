import pytest
from framework.dates.for_date import ForDate
from framework.utils.custom_assert import CustomAssert


@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2020,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2055,05,21'])
def test_interval(date_start, date_end, date_in_interval):
    obj_date = ForDate()
    CustomAssert.my_assert(obj_date.in_interval(date_start, date_end, date_in_interval)==True)

@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2000,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test2_interval(date_start, date_end, date_in_interval):
    obj_date = ForDate()
    CustomAssert.my_assert(obj_date.in_interval(date_start, date_end, date_in_interval))

@pytest.mark.parametrize('date', ['2029,07,22'])
def test_indiff(date):
    obj_date= ForDate()
    CustomAssert.my_assert(obj_date.date_difference(date))


# negative
@pytest.mark.parametrize('date', ['20uhjhh2'])
def test2_indiff(date):
    obj_date= ForDate()
    CustomAssert.my_assert(obj_date.date_difference(date))


@pytest.mark.parametrize('one_date', ['2029,05,22'])
@pytest.mark.parametrize('two_date', ['2029,05,22'])
def test_comparsdate(one_date, two_date):
    obj_date= ForDate()
    CustomAssert.my_assert(obj_date.compars_date(one_date, two_date))

# negative

@pytest.mark.parametrize('one_date', ['2029,05,22'])
@pytest.mark.parametrize('two_date', ['2009,15,22'])
def test2_comparsdate(date_1, two_date):
    obj_date= ForDate()
    CustomAssert.my_assert(obj_date.compars_date(date_1, two_date))
