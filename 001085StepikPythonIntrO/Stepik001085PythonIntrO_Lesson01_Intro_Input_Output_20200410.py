a = (10, 20, 13)  # объявление кортежа
b = tuple("Hello, World!")  # преобразование в кортеж
print(b[0])  # обращение к элементу
c = (1, 2, 3, (4, 5, 6))  # кортеж может содержать кортежи
print(c[3][0])  # обращение к элементу вложенного кортежа
# распаковка кортежа (не разобрался)
student = ("Шейх", "Мусса", "Python", 40)
name, surname, language, age = student
print(name)
print(surname)
# прикольно, интересно, где бы это использовать
print(tuple(range(1, 20)))  # генерация нумераций для списка
print(tuple(range(-100, -120, -1)))  # генерация убывающего диапазона
print(tuple(range(20)))  # генерация нумераций для списка

for (i) in range(1, 10, 2):
    print(i)

# перебор элементов кортежа
winter_months = ("декабрь", "январь", "февраль")
for i in winter_months:
    print(i, "- это зимний месяц")

for (i) in ("smile"):
    print(i, end=' ')
print()

colors = ("red", "green", "yellow")
fruits = ("apple", "pear")
for i in colors:
    for j in fruits:
        print(i, j)
