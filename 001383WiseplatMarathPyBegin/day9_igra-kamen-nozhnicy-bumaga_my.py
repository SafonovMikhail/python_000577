# -*- coding: utf-8 -*-
# import random

igrok1 = 0
igrok2 = 0
win = 0
draw = 0
lose = 0
list_choises = ['Камень', 'Ножницы', 'Бумага']


def verify(igrok, num):
    if num == 1:
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
    if num == 2:
        igrok = rnd2()
    return list_choises[1 - igrok]


def rnd2():
    import random
    choise2 = random.randint(1, 3)
    return choise2


import time

tm1 = time.localtime()
# print("%s-%s-%s %s:%s:%s" % (tm1[2], tm1[1], tm1[0], tm1[3], tm1[4], tm1[5]))

print("(Камень - 1, Ножницы - 2, Бумага - 3) Введите ваш номер:")
igrok1 = verify(igrok1, 1)
igrok2 = verify(igrok2, 2)
# Запись в файл
f = open('vybor_igrokov.txt', "w")  # открываем файл на запись
f.write("%s-%s-%s %s:%s:%s Игрок 1 выбрал %s" % (
tm1[2], tm1[1], tm1[0], tm1[3], tm1[4], tm1[5], igrok1) + "\n")  # записываем в файл 1ю строку
f.write("%s-%s-%s %s:%s:%s Игрок 2 выбрал %s" % (
tm1[2], tm1[1], tm1[0], tm1[3], tm1[4], tm1[5], igrok2))  # записываем в файл 2ю строку
f.close()  # закрываем файл — иначе в нем не отобразятся изменения

# Чтение из файла
f = open('vybor_igrokov.txt')  # открываем файл на запись
r = f.read()
print()
print("стандартный вывод: ")
print(r)
print()
