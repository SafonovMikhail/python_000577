'''
Задача «Список квадратов»
Условие
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
'''
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2, end=' ')
    i += 1
