a = int(input())
# a = 20
b = int(input())
# b = 80
step = -1
if a < b and step < 0:
    a, b = b, a
    print(tuple(range(a, b, step)))
else:
    print(tuple(range(a, b, step)))
