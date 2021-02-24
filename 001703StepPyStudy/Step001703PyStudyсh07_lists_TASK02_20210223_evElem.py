'''
Задача «Четные элементы»
Условие
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
'''
l1 = input().split()
# print(l1)
for i in range(len(l1)):
    l1[i] = int(l1[i])  # список изменяемый, преобразуем!
# print(l1)
for i in l1:
    if i % 2 == 0:
        print(i, end=' ')

# разработчики
s = input()
a = [int(s) for s in s.split()]  # задачи на закрепление конструкции. Все - объект!
for i in a:
    if int(i) % 2 == 0:
        print(i, end=' ')

# Svetlana Tetyusheva
a = [int(s) for s in input().split()] # !!!
for i in a:
    if i % 2 == 0:
        print(i, end=' ')
