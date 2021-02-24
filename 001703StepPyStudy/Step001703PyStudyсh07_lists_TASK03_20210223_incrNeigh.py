'''
Задача «Больше предыдущего»
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
'''
a = [int(s) for s in input().split()]
# print(a)
for i in range(len(a) - 1):
    if a[i + 1] > a[i]:
        print(a[i + 1], end=' ')

# разработчики
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])