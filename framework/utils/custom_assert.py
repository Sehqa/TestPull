
import trace
error_list = []


class CustomAssert(object):

    @staticmethod
    def my_assert(assert_condition, message=None):
        global error_list
        try:
            assert assert_condition
        except AssertionError as error:
            if(message==None):
               raise
            else:
                raise Exception(message)