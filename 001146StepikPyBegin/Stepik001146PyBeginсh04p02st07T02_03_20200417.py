# Задача 3. Напишите программу, которая по координатам точки,
# не лежащей на осях координат, определяет номер координатной
# четверти, в которой она находится.

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')
