import types
import inspect

error_list = []


class CustomAssert(object):
    @staticmethod
    def my_assert(assert_condition, message=None):
        global error_list
        if isinstance(assert_condition, types.FunctionType):
            try:
                assert_condition()
            except AssertionError as error:
                if message is not None:
                    error_list.append(message)
                else:
                    (file_path, line, function_name) = inspect.stack()[2][1:4]
                    error_list.append(
                        'Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))
        else:
            try:
                assert assert_condition
            except AssertionError:
                if message is not None:
                    error_list.append(message)
                else:
                    (file_path, line, function_name) = inspect.stack()[2][1:4]
                    error_list.append(
                        'Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))

    @staticmethod
    def show_error():
        global error_list
        if len(error_list) > 0:
            print('\n')
            print(error_list)
