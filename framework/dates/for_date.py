import datetime
import timestring


class ForDate(object):

    def in_interval(self,date_start, date_end, date_in_interval):
        date_start = timestring.Date(date_start).date
        date_end = timestring.Date(date_end).date
        date_in_interval = timestring.Date(date_in_interval).date
        return (date_start < date_in_interval < date_end)

    # Метод для вычисления разницы между текущей и заданной датой
    def date_difference(self,date):
        a = timestring.Date(date).date
        nowdate = datetime.datetime.now()
        if a < nowdate:
            return (nowdate - a)
        elif a > nowdate:
            return (a - nowdate)

    # метод для сравнения двух дат

    def compars_date(self,one_date, two_date):
        one_date = timestring.Date(one_date).date
        two_date = timestring.Date(two_date).date
        if one_date == two_date:
            return True
        else:
            return False
