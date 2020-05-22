a = int(input())
b = int(input())
if a % 2 != 0:
    a += 1
if b % 2 != 0:
    b += 1
print(abs(float(b - a)) // 2)
