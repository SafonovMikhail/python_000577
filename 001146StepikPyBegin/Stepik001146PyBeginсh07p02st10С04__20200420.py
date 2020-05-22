m = int(input())
n = int(input()) + 1
for i in range(m, n, ):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
        print(i)
