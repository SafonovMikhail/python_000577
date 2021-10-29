'''
Найти сумму всех элементов списка

[Массивы, Математика, Основы языка, Числа, Легко]

Напишите функцию, которая принимает список на вход,
и возвращает сумму всех элементов этого списка.

Примеры
sum_of_elements([20, 5, 5]) ➞ 30

sum_of_elements([10, 3, 0]) ➞ 13

sum_of_elements([-12, 10, 2]) ➞ 0
'''


def sum_of_elements(my_list):
    s_o_l = 0
    for i in my_list:
        s_o_l += i
    return s_o_l


my_lists = [10, 3, 0]
print(sum_of_elements(my_lists))
