'''
Stepik001146PyBeginсh07p08st08TASK04_20210123_my_other.py

(решил для высоты, но не для широкой стороны)

Дано нечетное натуральное число n. Напишите программу, которая печатает
равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:

*
**
***
****
***
**
*

Формат входных данных
На вход программе подается одно нечетное натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.
'''
# num1 = int(input())
num1 = 6
for i in range(1, num1 + 1):
    print("*" * i)
for i in range(num1 - 1, 0, -1):
    print("*" * i)
