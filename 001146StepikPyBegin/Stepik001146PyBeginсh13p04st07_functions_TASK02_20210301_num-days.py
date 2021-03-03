'''
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

Примечание 1. Гаранитируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

Примечание 2. Считайте, что год является невисокосным.

Примечание 3. Следующий программный код:

print(get_days(1))
print(get_days(2))
print(get_days(9))
должен выводить:

31
28
30

заготовка:
# объявление функции
def get_days(month):
    pass

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
'''


# объявление функции
def get_days(month):
    # result = -1
    if month in range(1,13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            result = 31
            return result
        elif month == 2:
            result = 28
            return result
        else:
            result = 30
            return result

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

# Александр Чуйко:
# https://stepik.org/lesson/331754/step/7?discussion=1581807&thread=solutions&unit=315133
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]

# Петр Баль:
# https://stepik.org/lesson/331754/step/7?discussion=1752513&thread=solutions&unit=315133
def get_days1(month):
    return (28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31)

