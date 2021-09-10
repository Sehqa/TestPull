import datetime
import timestring


class For_date(object):

    def ininterval(self,date1, date2, date3):
        date_a = timestring.Date(date1).date
        date_b = timestring.Date(date2).date
        date_c = timestring.Date(date3).date
        return (date_a < date_c < date_b)

    # Метод для вычисления разницы между текущей и заданной датой
    def datedifference(self,date):
        a = timestring.Date(date).date
        nowdate = datetime.datetime.now()
        if a < nowdate:
            return (nowdate - a)
        elif a > nowdate:
            return (a - nowdate)

    # метод для сравнения двух дат

    def comparsdate(self,date1, date2):
        date1 = timestring.Date(date1).date
        date2 = timestring.Date(date2).date
        if date1 == date2:
            return True
        else:
            return False
