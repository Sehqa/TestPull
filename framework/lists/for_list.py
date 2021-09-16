"""Метод для сравнения двух списков приведенных к типу type_value
или без приведения к типу если параметр tupe_value=False"""


class ListMet(object):
    @staticmethod
    def compars_mass(first_list=[], second_list=[], type_value=False):
        result_str = ''
        if len(first_list) != len(second_list):
            return False
        if type_value is False:
            for i in range(0, len(first_list)):
                if first_list[i] != second_list[i]:
                    result_str = result_str + 'Элементы ' + str(first_list[i]) + ' ' + str(second_list[i]) + ' ' + str(
                        i) + ' по индексу' + '\n'
        else:
            for i in range(0, len(first_list)):
                if eval(type_value + '({})'.format(first_list[i])) != eval(type_value +'({})'.format(second_list[i])):
                    result_str = result_str + 'Элементы ' + str(first_list[i]) + ' ' + str(
                        second_list[i]) + ' ' + str(i) + ' по индексу ' + '\n'
        if (len(result_str) > 0):
            return False
        else:
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            return True
