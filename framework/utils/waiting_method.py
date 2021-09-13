import datetime
import copy


class Utils(object):
    @staticmethod
    def wait_for_result(func, timeout, period):
        if func is not None:
            exit(0)
        start_time = datetime.datetime.now()
        now = datetime.datetime.now()
        call_time = copy.copy((now + datetime.timedelta(seconds=period)))  # запоминаем время следующего вызова
        timeout = copy.copy((now + datetime.timedelta(seconds=timeout)))  # запоминаем время таймаута
        while (now.time() < timeout.time()):
            now = datetime.datetime.now()
            if now.time() == call_time.time():  # если текущее время == времени следующего вызова
                if func is not None:
                    print('Фукнция вызывалась с ' + str(start_time.time()) + '  По ' + str(call_time.time()))
                    exit(0)
                call_time = (call_time + datetime.timedelta(seconds=period))  # обновляем время следующего вызова
        print('timeout')
