import datetime
import copy

result_list = []


class Utils(object):
    @staticmethod
    def wait_for_result(func, timeout, period, arg):
        result = func(arg)
        if (result != None):
            return True
        start_time = datetime.datetime.now()
        now = datetime.datetime.now()
        calltime = copy.copy((now + datetime.timedelta(seconds=period)))  # запоминаем время следующего вызова
        timeout = copy.copy((now + datetime.timedelta(seconds=timeout)))  # запоминаем время таймаута
        while (now.time() < timeout.time()):
            now = datetime.datetime.now()
            if (now.time() == calltime.time()):  # если текущее время == времени следующего вызова
                result = func(arg)
                if (result != None):
                    print('\n')
                    print('Фукнция вызывалась с ' + str(start_time.time()) + '  По ' + str(calltime.time()))
                    return True
                else:
                    calltime = (calltime + datetime.timedelta(seconds=period))  # обновляем время следующего вызова
        return False

    @staticmethod
    def add_in_result_list(n=0):
        global result_list
        if (len(result_list) > 2):
            return True
        else:
            result_list.append(n)
