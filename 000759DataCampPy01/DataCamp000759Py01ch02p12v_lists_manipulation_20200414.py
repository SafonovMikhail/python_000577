fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
print(fam)

print("# заменяем элемент списка: ")
fam[7] = 1.86
print(fam)

print("# заменяем ряд элементов списка: ")
print(fam[0:2])
fam[0:2] = ['lisa', 1.74]
print(fam)

print("# добавляем элемент к списку: ")
fam = fam + ['me', 1.79]
print(fam)

print("# удаляем элемент из списка [fam1]: ")
fam1 = fam[:]
print("fam1: ", fam1)
del (fam1[2])
print("fam1: ", fam1)

print("# создаем новый список [fam2] через фукнцию [list(fam)]: ")
fam2 = list(fam)
print("fam2:", fam2)
fam2[0] = 0
print("fam2:", fam2)
print("fam:", fam)
