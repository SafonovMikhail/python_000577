lst = ["Москва", "Санкт-Петербург", "Тверь", "Казань"]
print(lst)
print(lst[1:3])
lst2 = lst[2:4]
print(lst2)
lst3 = lst[-2:-1]  # правая граница не входит
print(lst3)

# создается ли копия списка
c = lst[:]
print(c, id(c))
print(lst, id(lst))

print("Создание списка через функцию-конструктор list(lst): ")
c = list(lst)
print(c, id(c))

print("# Присваивание срезам новых значений: ")
lst[1:3] = "Владимир", "Астрахань"
print(lst)