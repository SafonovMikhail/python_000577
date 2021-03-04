'''
Задача «Пересечение множеств»
Условие
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
'''
a = input()
b = input()
a1 = a.split()
b1 = b.split()
l1 = (list(set(a1) & set(b1)))
# print('l1',l1)
l2 = [int(elem) for elem in l1]
l2.sort()
# print('l2',l2)
l3 = [str(elem) for elem in l2]
print(' '.join(l3))

# решение разработчиков
print(*sorted(set(input().split()) & set(input().split()), key=int))

# Yana Charuyskaya
a = [int(i) for i in (set(input().split()) & set(input().split()))]
a.sort()
print(' '.join(str(i) for i in a))

# Леся Фундак
A = set([int(n) for n in input().split()])
B = set([int(n) for n in input().split()])
C = sorted(A & B)
for i in C:
    print(i, end=' ')

# Альбина Минибаева
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
r = a & b
print(*sorted(r))
