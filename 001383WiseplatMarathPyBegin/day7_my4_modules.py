import sys
from my_module import *

print("Введите что-то")
i1 = sys.stdin.readline() # считывание строки
print("Вы ввели %s" % i1)

print("Введите что-то 2")
i2 = sys.stdin.readline() # считывание строки
print("Вы ввели %s" % i2)

#################################################
# print("Подсчет №1")
podschet_monet_i_ih_ves(100, 1111, 1)
# print("Подсчет №2")
podschet_monet_i_ih_ves(1000, 1111, 2)

a1 = 100
b1 = 200
print("Площадь прямоугольника равна:", areaAB(a1, b1))  # пробел вставляется по умолчанию.
print("Площадь прямоугольника %s на %s равна:" % (a1, b1), areaAB(a1, b1))
# сначала подстановка (сервис), затем уже все остальное!
print("Площадь прямоугольника %s на %s равна: %s" % (a1, b1, areaAB(a1, b1)))
# использовать различные варианты!

for i in range(0, 1):
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    print("Площадь прямоугольника %s на %s равна: %s" % (a, b, areaAB(a, b)))
    print()  # вставим пустую строку (для благообразия)