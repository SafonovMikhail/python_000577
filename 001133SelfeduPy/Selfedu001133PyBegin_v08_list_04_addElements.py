digs = [1, 2, 3, 4]
print(digs)
digs = digs + [5]
print(digs)
digs += [6]
print(digs)

list = [1, 2, 3] + ["Москва", "Тверь"]
print(list)

print("Наличие элемента в списке: ")
print(3 in digs)  # возвращает [True]

print("Максимальное и минимальное значения: ")
digs = [1, 2, 3, 4]
print(digs)
print(max(digs))
print(min(digs))

print("Сортировки по возрастанию/убыванию")
d = [-1, 0, 5, 3, 2, 5]
print("исходный список: ", d)
print("сортировка по возрастанию: ", sorted(d))
print("сортировка по убыванию: ", sorted(d, reverse=True))
