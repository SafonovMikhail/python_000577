'''
Напишите программу, которая считывает целое число и выводит текст,
аналогичный приведенному в примере (пробелы важны!).

The next number for the number 1534 is 1535.
The previous number for the number 1534 is 1533.
'''
# n = int(input())
n = 1534
print(f'The next number for the number {n} is {n + 1}.')
print(f'The previous number for the number {n} is {n - 1}.')

n = int(input())
# n = 1534
print('The next number for the number', n, "is", str((n + 1))+'.')
print('The previous number for the number', n, "is", str((n - 1))+'.')
