sp1 = ["яблоки", "бананы", "капуста", "картошка", "грибы"]
print(sp1)
print(sp1[2])  # вызов элемента по индексу
sp1[3] = 'морковь'  # замена элемента
print(sp1)
sp1.append("сыр")
print(sp1)
del sp1[1]
print(sp1)
sp2 = [234, 235, 21, 43, 6565, 3344, 6564, 34]
sp3 = [3453, 'dfg', 667, 'df', 34]
sp4 = [sp2, sp3, sp1]  # создаем список списков
print(sp4)
print(sp4[1][1])
sp5 = [1, 2, 3]
sp6 = [4, 5, 6]
sp7 = sp5 + sp6  # сумма элементов списка
print(sp7)
sp8 = [5, 7]
sp9 = sp8 * 10 # единый список, элементов в 10 раз больше
print(sp9)
print(sp1[2:])
print(sp1[1:3])


