'''
вывести сумму нечетных чисел, вар.02
'''
while input("начинаем? (y/n): ") == "y":
    a, b = input().split()
    a = int(a)
    b = int(b)
    s = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            s += i
    print(s)
