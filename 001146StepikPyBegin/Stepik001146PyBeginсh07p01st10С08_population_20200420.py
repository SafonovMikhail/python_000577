m = float(input())
p = (float(input()) / 100)
n = int(input())
for i in range(n):
    print(i + 1, m)
    m = m + m * p
