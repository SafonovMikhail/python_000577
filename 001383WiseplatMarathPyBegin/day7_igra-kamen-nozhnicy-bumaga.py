# -*- coding: utf-8 -*-
igrok1 = 0
igrok2 = 0
win = 0
draw = 0
lose = 0
list_choises = ['Камень', 'Ножницы', 'Бумага']

def verify(igrok, num):
    igrok = int(input())
    while 1 < igrok > 3:
        print("Введен некорректный номер")
        print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок %s, введите ваш номер:" % num)
        igrok = int(input())
    if igrok == 1:
        print('Игрок %s выбрал %s' % (num, list_choises[1 - igrok]))
    elif igrok == 2:
        print('Игрок %s выбрал %s' % (num, list_choises[1 - igrok]))
    else:
        print('Игрок %s выбрал %s' % (num, list_choises[1 - igrok]))
    return list_choises[1 - igrok]

print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 1, введите ваш номер:")
igrok1 = verify(igrok1, 1)
igrok2 = verify(igrok2, 2)
