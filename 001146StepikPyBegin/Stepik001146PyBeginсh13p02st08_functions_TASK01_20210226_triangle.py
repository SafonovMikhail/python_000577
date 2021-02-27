'''
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

Sample Input 1:

*
9
Sample Output 1:

*
**
***
****
*****
****
***
**
*
Sample Input 2:

+
5
Sample Output 2:

+
++
+++
++
+
Sample Input 3:

?
7
Sample Output 3:

?
??
???
????
???
??
?
Заготовка:
# объявление функции
def draw_triangle(fill, base):
    pass

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


'''


def draw_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for i in range(base - base // 2, 0, -1):
        print(fill * i)


fill = input()
base = int(input())

draw_triangle(fill, base)


# форум:
# Vladislav Radostev
# https://stepik.org/lesson/333525/step/8?discussion=1673423&thread=solutions&unit=316953
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# Евгений Бичан
# https://stepik.org/lesson/333525/step/8?discussion=1771681&thread=solutions&unit=316953
# объявление функции
def draw_triangle(fill, base):
    print(*[fill * (min(i, base + 1 - i)) for i in range(1, base + 1)], sep="\n")


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# Максим Лютов
# https://stepik.org/lesson/333525/step/8?discussion=1653946&thread=solutions&unit=316953
# ¯\_(ツ)_/¯

# объявление функции
def draw_triangle(fill, base):
    h = base // 2 + 1
    print(*[fill * k for k in range(1, h)], sep='\n')
    print(*[fill * k for k in range(h, 0, -1)], sep='\n')


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
