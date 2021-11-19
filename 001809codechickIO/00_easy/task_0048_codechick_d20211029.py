'''
Деление нацело

[Валидация, Математика, Числа, Легко]

Функция получает на вход два числа: a и b.
Она должна вернуть True, если a можно разделить на b без остатка,
и False в противном случае.

Примеры
divides_evenly(98, 7) ➞ True
# 98/7 = 14

divides_evenly(85, 4) ➞ False
# 85/4 = 21.25
'''


def divides_evenly(a, b):
    if a % b == 0:
        flag = True
    else:
        flag = False
    return flag