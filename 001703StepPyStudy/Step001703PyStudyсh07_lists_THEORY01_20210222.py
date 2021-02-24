print()
# ----------------------------
print('# 7. Списки (lists)')
Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Primes)
print(Rainbow)
print()

# ----------------------------
print('# индексы (отрицательные)')
print(Primes[-1])  # 13
print(Primes[-6])  # 2
print()

# ----------------------------
print('# Изменение элементов списка')
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'красный'  # замена
print('Выведем радугу:')
for i in range(len(Rainbow)):
    print(Rainbow[i])
print()

# ----------------------------
print('# Списки: создание, считывание, вариант01')
# a = []  # заводим пустой список
# n = int(input())  # считываем количество элемент в списке
# for i in range(n):
#     new_element = int(input())  # считываем очередной элемент
#     a.append(new_element)  # добавляем его в список
#     # последние две строки можно было заменить одной:
#     # a.append(int(input()))
# print(a)
print()

# ----------------------------
print('# Списки: создание, считывание, вариант02')
# a = []
# for i in range(int(input())): # лаконично, в задачи!
#     a.append(int(input()))
# print(a)
print()

# ----------------------------
print('# Конкатенация, повторение')
a = [1, 2, 3]
print('a:', a)
b = [4, 5]
print('b:', b)
c = a + b
print('c = a + b:', c)
d = b * 3
print('d = b * 3:', d)
print([7, 8] + [9])
print([0, 1] * 3)
print()

# ----------------------------
print('# Списки: создание, считывание [2]')
# a = [0] * int(input())
# for i in range(len(a)):
#     a[i] = int(input())
print()

# ----------------------------
print('# Списки: вывод [1]')
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])
print()

# ----------------------------
print('# Списки: вывод [2]')
a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem, end=' ')
print()
print()

# ----------------------------
print('# из строки надо выбрать все цифры и сложить их в массив как числа')
# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
print('s:', s)
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:  # обратить внимание на констукцию для [find]
        digits.append(int(symbol))
print(digits)
print()
# ----------------------------
print('# 2. Методы split и join')
# на вход подаётся строка
# 1 2 3
# s = input()  # s == '1 2 3'
s = '1 2 3'
a = s.split()  # a == ['1', '2', '3']
print(a)
# ----------------------------
print('# Преобразование списка строк с список чисел.')
# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
print()
# ----------------------------
print('# "магия питона"')
# a = [int(s) for s in input().split()]
print()
# ----------------------------
print("# split '.' - необязательный аргумент")
a1 = '192.168.0.1'.split('.')
print(a1)
print()
# ----------------------------
print("# join:")
a = ['red', 'green', 'blue']
print(' '.join(a))
# вернёт red green blue
print(''.join(a))
# вернёт redgreenblue
print('***'.join(a))
# вернёт red***green***blue
print()
# ----------------------------
print("# ' '.join: вывести элементы списка, разделяя пробелами")
a = [1, 2, 3]
print(a)
print(' '.join([str(i) for i in a]))
# следующая строка, к сожалению, вызывает ошибку:
# print(' '.join(a))
print()
# ----------------------------
print("# 3. Генераторы списков:")
n = 5
a = [0] * n
print(a)
print()
# ----------------------------
print("# генератор 01:")
a = [0 for i in range(5)]
print()
# ----------------------------
print("# генератор 01: список квадратов чисел")
n = 5
b = [i ** 2 for i in range(n)]
print(b)
print(' '.join([str(i) for i in b]))
print()
# ----------------------------
print("# генератор 01: список случайных чисел")
from random import randrange

n = 10
a_rnd = [randrange(1, 10) for i in range(n)]
print(a_rnd)
print()
# ----------------------------
print("# генератор 01: список из стандартного ввода")
a_st_inp = [input('элемент: ') for i in range(int(input('число элементов: ')))]
print(a_st_inp)
print()
# ----------------------------
print("# 4. Срезы")

print()
# ----------------------------
print("# замена срезов: ")
A = [1, 2, 3, 4, 5]
print('исходный:', A)
A[2:4] = [7, 8, 9]
print('применили срез:', A) # >>> [1, 2, 7, 8, 9, 5]
print()
# ----------------------------
print("# замена срезов: три элемента")
A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40] # замена начиная с первого элемента
print('A:', A) # >>> A: [40, 2, 30, 4, 20, 6, 10]
print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
# ----------------------------
print("# split '.' - необязательный аргумент")

print()
