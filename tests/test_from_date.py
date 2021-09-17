import pytest
from framework.dates.for_date import DateUtils
from framework.utils.custom_assert import CustomAssert


@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2020,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test_interval(date_start, date_end, date_in_interval):
    obj_date = DateUtils()
    CustomAssert.my_assert(obj_date.check_in_interval(date_start, date_end, date_in_interval) == True)


@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2000,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test2_interval(date_start, date_end, date_in_interval):
    obj_date = DateUtils()
    CustomAssert.my_assert(obj_date.check_in_interval(date_start, date_end, date_in_interval) == True)


@pytest.mark.parametrize('year', [2020])
@pytest.mark.parametrize('month', [5])
@pytest.mark.parametrize('day', [21])
@pytest.mark.parametrize('hour', [12])
@pytest.mark.parametrize('minute', [12])
@pytest.mark.parametrize('seconds', [14])
@pytest.mark.parametrize('expected', [3])
def test_in_offset(year, month, day, hour, minute, seconds, expected):
    obj_date = DateUtils()
    CustomAssert.my_assert (obj_date.offset_calculation(year, month, day, hour, minute, seconds) == expected)


@pytest.mark.parametrize('year', [2020])
@pytest.mark.parametrize('month', [5])
@pytest.mark.parametrize('day', [21])
@pytest.mark.parametrize('hour', [12])
@pytest.mark.parametrize('minute', [12])
@pytest.mark.parametrize('seconds', [14])
@pytest.mark.parametrize('expected', [5])
def test2_in_offset(year, month, day, hour, minute, seconds, expected):
    obj_date = DateUtils()
    CustomAssert.my_assert((obj_date.offset_calculation(year, month, day, hour, minute, seconds) == expected))


@pytest.mark.parametrize('year_first_date', [2020])
@pytest.mark.parametrize('month_first_date', [5])
@pytest.mark.parametrize('day_first_date', [21])
@pytest.mark.parametrize('year_second_date', [2020])
@pytest.mark.parametrize('month_second_date', [5])
@pytest.mark.parametrize('day_second_date', [21])
def test_compars(year_first_date, month_first_date, day_first_date, year_second_date, month_second_date,
                  day_second_date):
    obj_date = DateUtils()
    CustomAssert.my_assert(obj_date.compars_date(year_first_date, month_first_date, day_first_date,
                                                 year_second_date, month_second_date, day_second_date))


@pytest.mark.parametrize('year_first_date', [2020])
@pytest.mark.parametrize('month_first_date', [5])
@pytest.mark.parametrize('day_first_date', [21])
@pytest.mark.parametrize('year_second_date', [2020])
@pytest.mark.parametrize('month_second_date', [5])
@pytest.mark.parametrize('day_second_date', [22])
def test2_compars(year_first_date, month_first_date, day_first_date, year_second_date, month_second_date,
                  day_second_date):
    obj_date = DateUtils()
    CustomAssert.my_assert(obj_date.compars_date(year_first_date, month_first_date, day_first_date,
                                                 year_second_date, month_second_date, day_second_date))
