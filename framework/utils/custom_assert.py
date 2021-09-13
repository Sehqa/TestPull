import types
import inspect
errlist = []

class CustomAssert(object):


    @staticmethod
    def my_assert(assert_condition, message=None):
        global errlist
        if isinstance(assert_condition, types.FunctionType):
            try:
                assert_condition()
            except AssertionError as error:
                if message is not None:
                    errlist.append(message)
                else:
                    (file_path, line, function_name) = inspect.stack()[2][1:4]
                    errlist.append(
                    'Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))
        else:
            try:
                assert assert_condition
            except AssertionError:
                if message is not None:
                    errlist.append(message)
                else:
                    (file_path, line, function_name) = inspect.stack()[2][1:4]
                    errlist.append(
                    'Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))

    @staticmethod
    def show_error():
        global errlist
        print(errlist)



