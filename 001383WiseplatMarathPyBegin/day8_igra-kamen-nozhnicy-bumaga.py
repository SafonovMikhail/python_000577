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


print("Введите ваш номер (Камень - 1, Ножницы - 2, Бумага - 3): ")
igrok1 = verify(igrok1, 1)
igrok2 = verify(igrok2, 2)
# Запись в файл
f = open('vybor_igrokov.txt', "w")  # открываем файл на запись
f.write("Игрок 1 выбрал %s" % (igrok1) + "\n")  # записываем в файл 1ю строку
f.write("Игрок 2 выбрал %s" % (igrok2))  # записываем в файл 2ю строку
f.close()  # закрываем файл — иначе в нем не отобразятся изменения

# Чтение из файла
f = open('vybor_igrokov.txt')  # открываем файл на запись
r = f.read()
print()
print("стандартный вывод: ")
print(r)
##############  остановочный блок [начало] ##############
import sys
sys.exit()  # позволяет выходить из оболочки при выполнении кода
##############  остановочный блок [конец] ##############
print()
print("lower(): ")
print(r.lower())
print()
print("upper(): ")
print(r.upper())
f.close()  # закрываем файл — иначе в нем не отобразятся изменения





