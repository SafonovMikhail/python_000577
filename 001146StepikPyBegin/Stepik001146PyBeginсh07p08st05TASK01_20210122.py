'''
Дано натуральное число (n<=9).
Напишите программу, которая печатает таблицу размером n×3 состоящую из данного числа
(числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n \times 3n×3 состоящую из данного числа.

Примечание. В конце строки может быть пробел.
'''
num = int(input())
# num = 8
for i in range(num):
    j = 0
    while j < 3:
        print(f'{num} ', end='')
        j += 1
    print()