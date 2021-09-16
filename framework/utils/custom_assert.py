
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
                error_list.append(error)
                CustomAssert.show_error()
            else:
                raise Exception(message)


    @staticmethod
    def show_error():
        if(len(error_list)>=1):
            for i in error_list:
                raise i
