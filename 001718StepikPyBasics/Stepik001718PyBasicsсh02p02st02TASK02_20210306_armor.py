'''
Максим начал играть в новую онлайн-игру, и в качестве приветственного бонуса ему подарили два комплекта брони с разными характеристиками. Помогите Максиму выбрать броню с максимальными характеристиками.

Формат входных данных

Два вещественных числа в различных строках - показатели защиты первой и второй брони соответственно.

Формат выходных данных

Максимальный показатель защиты из предложенных вариантов.

Sample Input 1:

47
19.9
Sample Output 1:

47.0
Sample Input 2:

109.8
1080.9
Sample Output 2:

1080.9
'''
n1 = float(input())
n2 = float(input())
if n2 > n1:
    print(n2)
else:
    print(n1)
