string = "Тестовая строка"  # строка - массив символов, список
print('len(string):', len(string))
i = 0
while i < len(string):
    print(string[i])
    i = i + 1

print()

list_ = [1, 2, 3, 66, 13]  # список символов
i = 0
while i < len(list_):
    print(list_[i])
    i = i + 1

print()

list_ = [1, 2, 3, 66, 13]
for el in list_: # цикл [for] выглядит лаконичнее
    print(el)
