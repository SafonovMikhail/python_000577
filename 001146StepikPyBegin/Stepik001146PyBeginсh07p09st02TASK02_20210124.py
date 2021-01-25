'''
Дано натуральное число n. Напишите программу, которая печатает численный треугольник
с высотой равной n, в соответствии с примером:

1
121
12321
1234321
123454321
...
'''

num1 = int(input())
# num1 = 4
for i in range(num1 + 1):
    count = 0
    for j in range(i):
        count += 1
        print(f"{count}", end="")
    for k in range(i, 1, -1):
        count -= 1
        print(f"{count}", end="")
    print()
