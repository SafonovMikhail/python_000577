m = int(input())
n = int(input()) + 1
if m < n:
    # n += 1
    for i in range(m, n):
        print(i)
else:
    n -= 1
    for i in range(m, n, -1):
        print(i)
