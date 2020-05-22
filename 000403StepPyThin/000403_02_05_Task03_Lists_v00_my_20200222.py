a = [int(g) for g in input().split()]
b = 0
for i in range(len(a)):
    b += a[i-1]
print(b)
