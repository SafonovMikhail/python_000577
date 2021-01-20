n = int(input("Введите число: "))
sum = 0
a, b = 0, 1
while b < n:
    print(b, end=', ')
    sum += b
    a, b = b, a + b
print()
print("Cумма чисел Фибоначчи равна: ", sum)
