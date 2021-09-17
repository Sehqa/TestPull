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
        call_time = copy.copy((now + datetime.timedelta(seconds=period)))  # запоминаем время следующего вызова
        timeout = copy.copy((now + datetime.timedelta(seconds=timeout)))  # запоминаем время таймаута
        while now.time() < timeout.time():
            now = datetime.datetime.now()
            if now.time() == call_time.time():  # если текущее время == времени следующего вызова
                result = func(arg)
                if result is not None:
                    print('\n')
                    print('Фукнция вызывалась с ' + str(start_time.time()) + '  По ' + str(call_time.time()))
                    return True
                else:
                    call_time = (call_time + datetime.timedelta(seconds=period))  # обновляем время следующего вызова
        return False

    @staticmethod
    def add_in_result_list(n=0):
        if len(result_list) > 2:
            result_list.clear()
            return True
        else:
            result_list.append(n)
