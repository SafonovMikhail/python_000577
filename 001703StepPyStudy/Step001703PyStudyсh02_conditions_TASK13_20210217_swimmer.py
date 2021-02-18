'''
Яша плавал в бассейне размером N × M метров и устал.
В этот момент он обнаружил, что находится на расстоянии x метров
от одного из длинных бортиков (не обязательно от ближайшего) и
y метров от одного из коротких бортиков. Какое минимальное
расстояние должен проплыть Яша, чтобы выбраться из бассейна
на бортик? Программа получает на вход числа N, M, x, y. Программа
должна вывести число метров, которое нужно проплыть Яше до бортика.
'''
m = int(input())
n = int(input())
x = int(input())
y = int(input())
height = n
width = m
if m > n:
    height = m
    width = n
dist_hor_left = x
dist_hor_right = width - x
dist_vert_bottom = y
dist_vert_top = height - y
dist_hor_min = 0
dist_vert_min = 0
if dist_hor_left < dist_hor_right:
    dist_hor_min = dist_hor_left
else:
    dist_hor_min = dist_hor_right
if dist_vert_bottom < dist_vert_top:
    dist_vert_min = dist_vert_bottom
else:
    dist_vert_min = dist_vert_top
if dist_vert_min > dist_hor_min:
    print(dist_hor_min)
else:
    print(dist_vert_min)
