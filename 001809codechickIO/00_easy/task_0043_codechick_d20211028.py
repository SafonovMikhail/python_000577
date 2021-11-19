'''
Числа, кратные 100
Алгебра
Валидация
Математика
Условия
Легко
Напишите функцию, которая принимает целое число и возвращает True, если оно делится на 100. В противном случае функция должна вернуть False.

Примеры
divisible(1) ➞ false

divisible(1000) ➞ true

divisible(100) ➞ true
'''


def divisible(num):
    if num % 100 == 0:
        flag = True
    else:
        flag = False
    return flag


print(divisible(10))
