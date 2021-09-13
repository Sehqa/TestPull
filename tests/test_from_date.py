import pytest
from framework.dates.for_date import ForDate
from smart_assertions import soft_assert




@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2020,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2055,05,21'])
def test_interval(date_start, date_end, date_in_interval):
    objdate = ForDate()
    soft_assert(objdate.in_interval(date_start, date_end, date_in_interval)==True,'Baaaad')





@pytest.mark.parametrize('date_start', ['2002,08,5'])
@pytest.mark.parametrize('date_end', ['2000,07,22'])
@pytest.mark.parametrize('date_in_interval', ['2005,05,21'])
def test2_interval(date_start, date_end, date_in_interval):
    objdate = ForDate()
    soft_assert(objdate.in_interval(date_start, date_end, date_in_interval))
  #  soft_assert(objdate.ininterval(date_start, date_end, date_in_interval))


@pytest.mark.parametrize('dat1', ['2029,07,22'])
def test_indiff(dat1):
    objdate= ForDate()
    soft_assert(objdate.date_difference(dat1))


# negative
@pytest.mark.parametrize('dat1', ['20uhjhh2'])
def test2_indiff(dat1):
    objdate= ForDate()
    soft_assert(objdate.date_difference(dat1))


@pytest.mark.parametrize('date_1', ['2029,05,22'])
@pytest.mark.parametrize('date_2', ['2029,05,22'])
def test_comparsdate(date_1, date_2):
    objdate= ForDate()
    assert(objdate.compars_date(date_1, date_2))


# negative

@pytest.mark.parametrize('date_1', ['2029,05,22'])
@pytest.mark.parametrize('date_2', ['2009,15,22'])
def test2_comparsdate(date_1, date_2):
    objdate= ForDate()
    assert(objdate.compars_date(date_1, date_2))
