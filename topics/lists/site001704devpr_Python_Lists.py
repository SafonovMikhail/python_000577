# List Comprehensions

# n = int(input())
n = 7
a = [i for i in range(n)]
print(a)  # [0, 1, 2, 3, 4, 5, 6]

# a = [i for i in range(int(input()))]
a = [i for i in range(7)]
print(a)  # [0, 1, 2, 3, 4, 5, 6]

# List Comprehensions как обработчик списков
# Задача [site001704devpr_Python_Lists.py:001][loop]:
# Пусть у нас есть список и нужно получить
# на базе него новый, который содержит элементы первого,
# возведенные в квадрат
a = [1, 2, 3, 4, 5, 6, 7]
b = []
for i in a:
    b.append(i ** 2)

print('a = {}\nb = {}'.format(a, b))
# >>> a = [1, 2, 3, 4, 5, 6, 7]
# >>> b = [1, 4, 9, 16, 25, 36, 49]

# Задача [site001704devpr_Python_Lists.py:002][lambda][map]:
# Пусть у нас есть список и нужно получить
# на базе него новый, который содержит элементы первого,
# возведенные в квадрат
a = [1, 2, 3, 4, 5, 6, 7]
b = list(map(lambda x: x ** 2, a))
print('a = {}\nb = {}'.format(a, b))
# >>> a = [1, 2, 3, 4, 5, 6, 7]
# >>> b = [1, 4, 9, 16, 25, 36, 49]

# Задача [site001704devpr_Python_Lists.py:003][list comprehension]:
# Пусть у нас есть список и нужно получить
# на базе него новый, который содержит элементы первого,
# возведенные в квадрат
a = [1, 2, 3, 4, 5, 6, 7]
b = [i ** 2 for i in a]
print('a = {}\nb = {}'.format(a, b))
# >>> a = [1, 2, 3, 4, 5, 6, 7]
# >>> b = [1, 4, 9, 16, 25, 36, 49]

# Задача [site001704devpr_Python_Lists.py:004][lambda][filter]:
a = [1, 2, 3, 4, 5, 6, 7]
b = list(filter(lambda x: x % 2 == 0, a))  # выбираем список четных чисел
print('a = {}\nb = {}'.format(a, b))
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [2, 4, 6]

# Задача [site001704devpr_Python_Lists.py:005][списковое включение]:
a = [1, 2, 3, 4, 5, 6, 7]
b = [i for i in a if i % 2 == 0]
print('a = {}\nb = {}'.format(a, b))
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [2, 4, 6]

# Слайсы / Срезы
print('# Слайсы / Срезы:')
a = [i for i in range(10)]
print(a)
# Получить копию списка
print('', a[:])
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Получить первые пять элементов списка
print('Получить первые пять элементов списка:', a[0:5])
# >>> [0, 1, 2, 3, 4]
# Получить элементы с 3-го по 7-ой
print('Получить элементы с 3-го по 7-ой:', a[2:7])
# >>> [2, 3, 4, 5, 6]
# Взять из списка элементы с шагом 2
print('Взять из списка элементы с шагом 2:', a[::2])
# >>> [0, 2, 4, 6, 8]
# Взять из списка элементы со 2-го по 8-ой с шагом 2
print('Взять из списка элементы со 2-го по 8-ой с шагом 2:', a[1:8:2])
# >>> [1, 3, 5, 7]

print('Слайсы можно определить заранее:')
s1 = slice(0, 5, 1)
print(a[s1])
# >>> [0, 1, 2, 3, 4]

s2 = slice(1, 8, 2)
print(a[s2])
# >>> [1, 3, 5, 7]

print()
# Типо “List Comprehensions”… в генераторном режиме
import sys

a = [i for i in range(10)]
print(type(a))
print(sys.getsizeof(a))

b = (i for i in range(10))
print(type(b))
print(sys.getsizeof(b))
print()
a = [i for i in range(10000)]
print(type(a))
print(sys.getsizeof(a))

b = (i for i in range(10000))
print(type(b))
print(sys.getsizeof(b))
