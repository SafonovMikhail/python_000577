# создание функций

#####################   03  #####################
# видимость переменных
p = 100


def pab():
    r = 10
    h = 20
    print(p, r, h)

print("Результат фукнции [pab()]: ")
pab()


#####################   02  #####################
def areaAB(a, b):
    '''расчет площади геометрической фигуры'''
    return a * b


#####################   01  #####################
def podschet_monet_i_ih_ves(moneti, ves, nomer):
    '''Расчет монет и их вес'''
    print("Подсчет №%s" % nomer)
    print("Всего вес монет: %s" % (moneti * ves))


#################################################
# print("Подсчет №1")
podschet_monet_i_ih_ves(100, 1111, 1)
# print("Подсчет №2")
podschet_monet_i_ih_ves(1000, 1111, 3)

a1 = 100
b1 = 200
print("Площадь прямоугольника равна:", areaAB(a1, b1))  # пробел вставляется по умолчанию.
print("Площадь прямоугольника %s на %s равна:" % (a1, b1), areaAB(a1, b1))
# сначала подстановка (сервис), затем уже все остальное!
print("Площадь прямоугольника %s на %s равна: %s" % (a1, b1, areaAB(a1, b1)))
# использовать различные варианты!

for i in range(0, 3):
    a = int(input("Введите а: "))
    b = int(input("Введите а: "))
    print("Площадь прямоугольника %s на %s равна: %s" % (a, b, areaAB(a, b)))
    print()  # вставим пустую строку (для благообразия)