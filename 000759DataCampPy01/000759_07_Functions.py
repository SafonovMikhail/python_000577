# def sum(var1,var2):
#     var3=var1+var2
#     return var3
# print(var3)

num1 = 1000
num2 = 2000


def HW():  # no prameters!
    print("HelloWorld!")


def addNumbers1(num1, num2):
    sum = num1 + num2
    return sum


def addNumbers2(num1, num2):
    sum = num1 + num2
    # return sum
    return num1, num2, sum
    # не понятно, каковы могут быть еще варианты возвращаемого значения, кроме значения, что в функции?
    # возвращает список?
    #


# Вызываем фукнции с возвращаемым значением и
# без возвращаемого значения

print("вызов функции HW")
HW()
print("\naddNumbers1(1,2):")  # не перегружать синтаксис, можно было бы принт написать в одну строку
print(addNumbers1(1, 2))
print("\naddNumbers2(1,2):")  #
print(addNumbers2(1, 2))
print("\n", num1)
# print("\n" + (str) num2) # пробел: приведение типов.
'''
переменные num1 и num2 не видны внутри функции
так называемые локальные переменные!
'''

'''
очень крутой вывод: мы используем функцию принт (print()) и 
в скобках передаем параметры, которые должны быть выведены на печать
только это встроенная фукнция (built-in), т.к. часто используется.
Хорошо бы привести код этой фукнции (в проге говорится, что это сотни строк кода)
'''

'''
изучать комплексные числа! Обязательно, чтобы не впадать в ступор (на будущее)
'''
