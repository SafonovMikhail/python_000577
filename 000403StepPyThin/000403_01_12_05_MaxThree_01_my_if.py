a = int(input())
b = int(input())
c = int(input())
if a - b < 0:
    a, b = b, a
if a - c < 0:
    a, c = c, a
if b - c < 0:
    b, c = c, b
print(a)
print(c)
print(b)

