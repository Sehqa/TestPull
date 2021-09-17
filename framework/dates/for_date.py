import datetime
import timestring
from datetime import datetime, timedelta
from dateutil import tz


class DateUtils(object):

    def check_in_interval(self, date_start, date_end, date_in_interval):
        date_start = timestring.Date(date_start).date
        date_end = timestring.Date(date_end).date
        date_in_interval = timestring.Date(date_in_interval).date
        return (date_start < date_in_interval < date_end)

    # Метод для вычисления cмещения
    def offset_calculation(self, year, month, day, hour, minute, seconds):
        blr_timezone = tz.gettz('Europe/Minsk')
        date = datetime(year, month, day, hour, minute, seconds, 0, tzinfo=blr_timezone)
        return date.utcoffset() / timedelta(hours=1)

    # метод для сравнения двух дат

    def compars_date(self, year_first_date=0000, month_first_date=0, day_first_date=0,
                     year_second_date=0, month_second_date=0, day_second_date=0):
        blr_timezone = tz.gettz('Europe/Minsk')
        first_date = datetime(year_first_date, month_first_date, day_first_date, tzinfo=blr_timezone)
        second_date = datetime(year_second_date, month_second_date, day_second_date, tzinfo=blr_timezone)
        if first_date == second_date:
            return True
        else:
            return False
