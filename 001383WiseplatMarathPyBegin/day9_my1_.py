####### day09vid01_18:01 ### [import pickle] #######
print("####### day09vid01_18:01 ### [import pickle] #######")

import pickle  # позволяет сохранять сложные объекты и извлекать из них значения.

game = {"life": 5, "armor": 7, "level": 100}  # создаем объект
file1 = open("day09_pickle_test.txt", "wb")  # открываем для побитовой записи
pickle.dump(game, file1)  # записываем в открытый файл данные
file1.close()

load_file = open("day09_pickle_test.txt", "rb")  # [rb] побитовое чтение файла
loaded = pickle.load(load_file)  # можем считать объект, который сохранили.
load_file.close()

print(loaded)

##############  остановочный блок [начало] ##############
import sys

sys.exit()  # позволяет выходить из оболочки при выполнении кода
##############  остановочный блок [конец] ##############


####### day09vid01_14:30 ### [import time] #######
print("####### day09vid01_14:30 ### [import time] #######")
import time

print(time.time())  # выводит текущее время (?! формат)
print(time.asctime())  # время в привычном виде
print(time.localtime())  # время в виде объекта (можно обращаться по параметрам)
t1 = time.localtime()
print("Year =", t1[0])  # объект - список, обращаемся к нулевому элементу
print("Year =", t1.tm_year)
for i in range(1, 5):
    print(i)
    time.sleep(1)  # задержка (в секундах)

####### day09vid01_12:00 ### [import sys] #######
print("####### day09vid01_12:00 ### [import sys] #######")

import sys

# sys.exit()  # позволяет выходить из оболочки при выполнении кода

in1 = sys.stdin.readline()  # считываем пользовательский ввод на экране
print(in1)
sys.stdout.write(in1)  # вывод на экран
print(sys.version)

# sys.exit() # позволяет выходить из оболочки при выполнении кода


####### day09vid01_05:51 ### [import random] #######
print("####### day09vid01_05:51 ### [import random] #######")
import random

print("randint(1,100): ", random.randint(1, 100))
num = random.randint(1, 100)
while True:
    print("Введите число от 1 до 100:")
    num1 = int(input())
    if num1 == num:
        print("Вы угадали")
        break
    else:
        print("Не угадали")
    if num1 == 1000:  # Таким образом выводится подсказка! Очень удобно!
        print("Загаданное число %s" % num)

print("#########   part2 - списки   #########")
sp1 = ["ауди", "бмв", "мерседес", "опель"]  # необходимо выбрать случайный элемент из списка
print("choice(sp1): ", random.choice(sp1))

####### day09vid01_04:00 ### [import keword] #######
print("####### day09vid01_04:00 ### [import keword] #######")

import keyword

print('iskeyword("if"): ', keyword.iskeyword("if"))

####### day09vid01_00:00 ### [import copy] #######
print("####### day08vid01_20:28 ### [open] #######")

import copy


class Auto():  # храним количество колес машины
    pass  # pass: пока просто создали класс, ничего в нем не пишем.


my_auto1 = Auto()  # создали новый объект, в который записали экземпляр класса Auto()
my_auto1.wheels = 4  # в объекте создаем переменную, количество колес
my_auto2 = copy.copy(my_auto1)
my_auto2.wheels = 2
print(my_auto1.wheels, my_auto2.wheels)
