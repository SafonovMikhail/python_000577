'''
Шахматный конь ходит буквой “Г” — на две клетки по вертикали
в любом направлении и на одну клетку по горизонтали, или наоборот.
Даны две различные клетки шахматной доски, определите, может ли
конь попасть с первой клетки на вторую одним ходом.
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dist_hor = x2 - x1
dist_vert = y2 - y1
if dist_vert < 0:
    dist_vert = dist_vert * -1
if dist_hor < 0:
    dist_hor = dist_hor * -1
if x2 < 1 or x2 > 8:
    print('NO')
elif dist_vert > 2 or dist_hor > 2:
    print('NO')
elif x1 == x2 or y1 == y2:
    print('NO')
elif (x2 - x1) / (y2 - y1) == 1 or (x2 - x1) / (y2 - y1) == -1:
    print('NO')
else:
    print('YES')