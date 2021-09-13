import datetime
import functools
import time


class HttpLogger(object):


    @staticmethod
    def logger(level=1, message=None):
        def decorator(func):
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
                        ang.write(str(result.url+' Status code: '+str(result.status_code)+' '+str(result.text)+' '\
                                      +'Time '+str(datetime.datetime.now())+'  '+str(message)))
                return func(*args, **kwargs)

            return wrapper

        return decorator
