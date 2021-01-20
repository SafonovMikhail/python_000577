# -*- coding: utf-8 -*-
# import random

igrok1 = 0
igrok2 = 0
win = 0
draw = 0
lose = 0
list_choises = [0,'Камень', 'Ножницы', 'Бумага']

def rnd2():
    import random
    choise2 = random.randint(1, 3)
    return choise2

def verify(igrok, num):
    if num == 1:
        igrok = int(input())
        while 1 < igrok > 3:
            print("Введен некорректный номер")
            print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок %s, введите ваш номер:" % num)
            igrok = int(input())
    if num == 2:
        igrok = rnd2()
    return list_choises[igrok]

import time

tm1 = time.localtime()
# print("%s-%s-%s %s:%s:%s" % (tm1[2], tm1[1], tm1[0], tm1[3], tm1[4], tm1[5]))

print("(Камень - 1, Ножницы - 2, Бумага - 3) Введите ваш номер:")
igrok1 = verify(igrok1, 1)
igrok2 = verify(igrok2, 2)
# Запись в файл
record_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())  # интересная передача значений.
f = open('vybor_igrokov.txt', "a")  # открываем файл на запись
f.write(record_time + " " + "Игрок 1 выбрал %s" % igrok1 + "\n")  # записываем в файл 1ю строку со временем
f.write(record_time + " " + "Игрок 2 выбрал %s" % igrok2 + "\n")  # записываем в файл 2ю строку со временем
f.close()  # закрываем файл — иначе в нем не отобразятся изменения

# Чтение из файла
f = open('vybor_igrokov.txt')  # открываем файл на запись
r = f.read()
f.close()  # закрываем файл — иначе в нем не отобразятся изменения
print()
print("стандартный вывод: ")
print(r)
print()


import pickle  # позволяет сохранять сложные объекты и извлекать из них значения.

# запись в дамп
game = {"Игрок 1": igrok1, "Игрок 2": igrok2}  # создаем объект
file1 = open("vars_igrokov.txt", "wb")  # открываем для побитовой записи
pickle.dump(game, file1)  # записываем в открытый файл данные
file1.close()

# Чтение из дампа
load_file = open("vars_igrokov.txt", "rb")  # [rb] побитовое чтение файла
loaded = pickle.load(load_file)  # можем считать объект, который сохранили.
load_file.close()
print(loaded)