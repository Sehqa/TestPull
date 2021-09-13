import datetime
import functools
import os
import time


class HttpLogger(object):
    __instance = None

    @staticmethod
    def inst():
        if HttpLogger.__instance is None:
            HttpLogger.__instance = HttpLogger()
        return HttpLogger.__instance

    @staticmethod
    def info(level=1, message=None, log_print=False):
        def actual_decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if level == 1:
                    with open('log.txt', 'w') as ang:
                        ang.write(str(result.url+' Status code: '+str(result.text)))
                if level == 2:
                    with open('log.txt', 'w') as ang:
                        ang.write(str(result.url+' Status code: '+str(result.status_code)))
                if level == 3:
                    t = time.time()
                    with open('log.txt', 'w') as ang:
                        ang.write(str(result.url+' Status code: '+str(result.status_code)+' '+str(result.text)+' '+str(datetime.datetime.now())+'  '+str(message)))
                if message is not None:
                    if log_print:
                        print('log')
                return func(*args, **kwargs)

            return wrapper

        return actual_decorator
