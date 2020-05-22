print("# создание списка из фиксированного числа значений")
N = 10
A = [x ** 2 for x in range(N)]
print(A)

print("# создание списка из квадратов значений, совмещенного с условем (четность)")
N = 10
A = [x ** 2 for x in range(N) if x % 2 == 0]
print(A)

cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
# A = [i  for i in cities if len(i) < 7]
# более ясная запись
A = [city for city in cities if len(city) < 7]

print(A)



# rnd = [(math.random()) * 100 for i in range(100)]
# print(rnd)
print((math.rnd()) * 100)

