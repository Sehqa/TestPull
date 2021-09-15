import datetime
import timestring
from datetime import datetime, timedelta
from dateutil import tz

class ForDate(object):

    def check_interval(self,date_start, date_end, date_in_interval):
        date_start = timestring.Date(date_start).date
        date_end = timestring.Date(date_end).date
        date_in_interval = timestring.Date(date_in_interval).date
        return (date_start < date_in_interval < date_end)

    # Метод для вычисления cмещения
    def date_difference(self,year,month,day,hour,minute,seconds):
        BLR = tz.gettz('Europe/Minsk')
        dt1 = datetime(year,month,day,hour, minute,seconds, 0, tzinfo=BLR)
        return (dt1.utcoffset() / timedelta(hours=1))

    # метод для сравнения двух дат

    def compars_date(self,one_date, two_date):
        one_date = timestring.Date(one_date).date
        two_date = timestring.Date(two_date).date
        if one_date == two_date:
            return True
        else:
            return False
