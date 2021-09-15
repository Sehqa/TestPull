
import trace
error_list = []


class CustomAssert(object):
    @staticmethod
    def show_error():
        global error_list
        if len(error_list) > 0:
            trace (error_list)

    @staticmethod
    def my_assert(assert_condition, message=None):
        global error_list
        try:
            assert assert_condition
        except AssertionError as error:
            error_list.append(error)