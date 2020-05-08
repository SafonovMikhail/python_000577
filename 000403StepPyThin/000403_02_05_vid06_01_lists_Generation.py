a = [0] * 5
print(a)
b = [0 for i in range(5)]
print(b)
c = [i * i for i in range(5)]
print(c)
# заполняем список значениями через пробел
d = [int(i) for i in input().split()]
print("d: ", d)
