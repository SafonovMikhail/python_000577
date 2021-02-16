'''
Заданы две клетки шахматной доски. Если они покрашены в один цвет,
то выведите слово YES, а если в разные цвета — то NO. Программа
получает на вход четыре числа от 1 до 8 каждое, задающие номер
столбца и номер строки сначала для первой клетки, потом для второй клетки.
'''
hor1 = int(input())
vert1 = int(input())
hor2 = int(input())
vert2 = int(input())

if ((hor1 + vert1) % 2 == 0) and ((hor2 + vert2) % 2 == 0):
    print('YES')
elif ((hor1 + vert1) % 2 != 0) and ((hor2 + vert2) % 2 != 0):
    print('YES')
else:
    print('NO')
# elif ((hor1 + vert1) % 2 == 0) and ((hor2 + vert2) % 2 != 0):
#     print('NO')
# elif ((hor1 + vert1) % 2 != 0) and ((hor2 + vert2) % 2 == 0):
#     print('NO')


