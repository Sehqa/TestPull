"""Метод для сравнения двух списков приведенных к конкретному типу type_value
или без приведения к типу если параметр tupe_value=False"""

class ListMet():
    def compars_mass(self,first_list, second_list, type_value=False):
        resultstr=''
        result_list=[]
        if len(first_list)!=len(second_list):
            return False
        if type_value is False:
            for i in range(0, len(first_list)):
                if first_list[i] != second_list[i]:
                    resultstr=resultstr+'Элементы '+str(first_list[i])+' '+str(second_list[i])+' '+str(i)+' по индексу'+'\n'
                   # return first_list[i], second_list[i], i
        else:
            for i in range(0, len(first_list)):
                if eval(type_value + '({})'.format(first_list[i])) != eval(type_value +
                    '({})'.format(second_list[i])):
                    resultstr = resultstr + 'Элементы ' + str(first_list[i]) + ' ' + str(
                        second_list[i]) + ' ' + str(i) + ' по индексу ' + '\n'
        if(len(resultstr)>0):
            print (resultstr)
            return False
        else:
            return True
                    #return (first_list[i], second_list[i], i)
