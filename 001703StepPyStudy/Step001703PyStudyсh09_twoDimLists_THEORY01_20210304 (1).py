a = [[1, 2, 3], [4, 5, 6]]
print('a:', a)
print('a[0]:', a[0])
print('a[1]:', a[1])
b = a[0]
print("b = a[0]")
print('b:', b)
print('a[0][2]:', a[0][2])
a[0][1] = 7
print('a[0][1] = 7')
print('a:', a)  # [[1, 7, 3], [4, 5, 6]]
print('b:', b)  # [1, 7, 3]
b[2] = 9
print('b[2] = 9')
print('a[0]:', a[0])  # [1, 7, 9]
print('b:', b)  # [1, 7, 9]
print()
print("вывод вложенных списков:")
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print('вывод с помощью for:')
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
print('метод join():')
for row in a:
    print(' '.join([str(elem) for elem in row]))  # разобраться
print('сумма всех элементов массива (по индексам):')
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)
print('сумма всех элементов массива (по элементам строк):')
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)
# -------------------------------
print('2. Создание вложенных списков')
n = 3
m = 4
a = [[0] * m] * n
a[0][0] = 5
print(a[1][0])
print(a[2][0])
print('Создание вложенных списков: ссылка на другой элемент')
n = 3
m = 4
a = [0] * n  # создаем три элемента
print(a)
for i in range(n):
    a[i] = [0] * m
print(a)
print()
print('Создание вложенных списков: append()')
n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)
print(a)
print()
print('Создание вложенных списков: генератор')
n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
print()
# -------------------------------
print('3. Ввод двумерного массива')
# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
print(a)
print()
print('Ввод двумерного массива: без использования сложных вложенных вызовов функций')
# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print(a)
print()
print('Ввод двумерного массива: генератор')
# в первой строке ввода идёт количество строк массива
n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)
print()
print()
# -------------------------------
print('4. Пример обработки двумерного массива')
