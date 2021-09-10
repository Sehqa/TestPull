import datetime
import requests


class Utils(object):

    @staticmethod
    def oncelog(func):
        def wrapper(*args):
            print(*args)
            request_on_url = requests.get(args[1])
            if args[2] == 1:
                with open(args[0], 'w') as ang:
                    ang.write(str(args[1] + request_on_url.text))
                result = func(*args)
            elif args[2] == 2:
                with open(args[0], 'w') as ang:
                    ang.write(str(args[1] + '  ' + str(request_on_url.status_code)))
                result = func(*args)
            elif args[2] == 3:
                with open(args[0], 'w') as ang:
                    currenttime = datetime.datetime.now().time()
                    ang.write(str(args[1] + '  ' + str(request_on_url.status_code) + ' ' + str(
                        currenttime) + request_on_url.text))
                result = func(*args)
            return result
        return wrapper



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


