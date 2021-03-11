'''
Убывающий ряд

С клавиатуры вводятся целые числа a > b.
Выведите убывающую последовательность чисел по одному числу в строке.

Sample Input:

-2
-8
Sample Output:

-2
-3
-4
-5
-6
-7
'''
a = int(input())
b = int(input())
for i in range(a, b, -1):
    print(i)

# f01
print(*tuple(range(int(input()), int(input()), -1)), sep='\n')

# f02
for i in range(int(input()), int(input()), -1): print(i)

# f03
a, b = (int(input()) for _ in range(2))
out = tuple(i for i in range(a, b, -1))
print(*out, sep='\n')

# f04
print(*[i for i in range(int(input()), int(input()), -1)], sep='\n')

# f05
''' range '''
print(*range(int(input()), int(input()), -1), sep="\n")

# f06
a, b = int(input()), int(input())
for i in range(a, b, -1):
    print(i)

# f07
a, b = int(input()), int(input())
for i in sorted(tuple(range(b + 1, a + 1)), reverse=True):
    print(i)

# f08
a = int(input())
b = int(input())
i = a
if a > b:
    while i != b:
        print(i)
        i = i - 1

# f09
a, b = int(input()), int(input())
for i in reversed(range(b + 1, a + 1)):
    print(i)

# f09
a = int(input())
b = int(input())
list = []
for i in range(b + 1, a + 1):
    list.append(i)
list.reverse()
for i in list:
    print(i)

# f10
a, b = int(input()), int(input())
if a > b:
    c = tuple(range(a, b, -1))
#    print(c)
    for i in range(a-b):
        print(c[i])

# f11
a = int(input())
b = int(input())
for i in range(-a, -b):
    print(-i)

# f12
a, b = [int(input()) for i in range(2)]
print(*tuple(range(a, b, -1)), sep = "\n")

# f13
a=int(input())
b=int(input())
c=(tuple(range(b+1, a+1)))
for i in reversed(c):
    print(i)

# f14
a, b = [int(input()) for i in 'aa']
for i in range(a, b, -1):
    print(i)


