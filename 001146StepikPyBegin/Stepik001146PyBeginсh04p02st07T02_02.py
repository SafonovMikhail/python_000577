# Задача 2. Напишите программу, которая проверяет, что все три цифры трёхзначного числа различны.
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1: # интересно
    print('Цифры различны')
else:
    print('Цифры не различны')
