import pytest
from framework.dates.for_date import ForDate
from framework.utils.custom_assert import CustomAssert


@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2020,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test_interval(date_start, date_end, date_in_interval):
    obj_date = ForDate()
    CustomAssert.my_assert(obj_date.check_interval(date_start, date_end, date_in_interval) == True)


@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2000,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test2_interval(date_start, date_end, date_in_interval):
    obj_date = ForDate()
    CustomAssert.my_assert(obj_date.check_interval(date_start, date_end, date_in_interval))


@pytest.mark.parametrize('year', [2020])
@pytest.mark.parametrize('month', [5])
@pytest.mark.parametrize('day', [21])
@pytest.mark.parametrize('hour', [12])
@pytest.mark.parametrize('minute', [12])
@pytest.mark.parametrize('seconds', [14])
@pytest.mark.parametrize('expected', [3])
def test_in_diff(year, month, day, hour, minute, seconds, expected):
    obj_date = ForDate()
    assert (obj_date.date_difference(year, month, day, hour, minute, seconds) == expected)


@pytest.mark.parametrize('year', [2020])
@pytest.mark.parametrize('month', [5])
@pytest.mark.parametrize('day', [21])
@pytest.mark.parametrize('hour', [12])
@pytest.mark.parametrize('minute', [12])
@pytest.mark.parametrize('seconds', [14])
@pytest.mark.parametrize('expected', [5])
def test2_in_diff(year, month, day, hour, minute, seconds, expected):
    obj_date = ForDate()
    CustomAssert.my_assert((obj_date.date_difference(year, month, day, hour, minute, seconds) == expected))


@pytest.mark.parametrize('one_date', ['2029,05,22'])
@pytest.mark.parametrize('two_date', ['2029,05,22'])
def test_compars_sdate(one_date, two_date):
    obj_date = ForDate()
    assert (obj_date.compars_date(one_date, two_date))


@pytest.mark.parametrize('year_first_date', [2020])
@pytest.mark.parametrize('month_first_date', [5])
@pytest.mark.parametrize('day_first_date', [21])
@pytest.mark.parametrize('year_second_date', [2020])
@pytest.mark.parametrize('month_second_date', [5])
@pytest.mark.parametrize('day_second_date', [21])
def test4_compars(year_first_date, month_first_date, day_first_date, year_second_date, month_second_date,
                  day_second_date):
    obj_date = ForDate()
    assert (
        obj_date.compars2_date(year_first_date, month_first_date, day_first_date, year_second_date, month_second_date,
                               day_second_date))


# negative

@pytest.mark.parametrize('one_date', ['2029,05,22'])
@pytest.mark.parametrize('two_date', ['2009,15,22'])
def test2_compars_date(one_date, two_date):
    obj_date = ForDate()
    CustomAssert.my_assert(obj_date.compars_date(one_date, two_date))
