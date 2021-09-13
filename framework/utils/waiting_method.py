import datetime
import copy

class Utils(object):
    @staticmethod
    def wait_for_result(func, timeout, period):
        if (func != None):
            exit(0)
        start_time = datetime.datetime.now()
        now = datetime.datetime.now()
        calltime = copy.copy((now + datetime.timedelta(seconds=period)))  # запоминаем время следующего вызова
        timeout = copy.copy((now + datetime.timedelta(seconds=timeout)))  # запоминаем время таймаута
        while (now.time() < timeout.time()):
            now = datetime.datetime.now()
            if (now.time() == calltime.time()):  # если текущее время == времени следующего вызова
                if (func != None):
                    print('Фукнция вызывалась с ' + str(start_time.time()) + '  По ' + str(calltime.time()))
                    exit(0)
                print(datetime.datetime.now().time().second)
                calltime = (calltime + datetime.timedelta(seconds=period))  # обновляем время следующего вызова
        print('timeout')
