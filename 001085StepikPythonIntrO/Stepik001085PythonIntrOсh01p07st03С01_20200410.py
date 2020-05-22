a = int(input())
b = int(input())
if b > a:
    print(tuple(range(a, b)))  # [a,b)
if a > b:
    print(tuple(range(b, a)))  # [b,a)
