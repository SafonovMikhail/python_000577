'''
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

Примечание 2. Следующий программный код:

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
должен выводить:

1
2
4

заготовка:
# объявление функции
def number_of_factors(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
'''


# объявление функции
def number_of_factors(num):
    count_factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count_factors += 1
    # print(count_factors)
    return count_factors


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
