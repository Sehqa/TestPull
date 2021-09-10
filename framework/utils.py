import datetime
import requests


class Utils(object):



    #для проверки ожидания
    def testfunc(dd):
        return True

    #метод ожидания
    @staticmethod
    def mainfunc(testfun, timeout, period):
        tim = timeout
        shet = 0
        for i in range(0, timeout):
            if testfun:
                return 'Success'
            elif tim <= 0:
                return 'timeout'
            else:
                shet = shet + 5
                tim = tim - period
                if testfun:
                    return print('Функция ' + 'вызывалась в течении ' + str(shet) + ' секунд')
                else:
                    datetime.time.sleep(5)

