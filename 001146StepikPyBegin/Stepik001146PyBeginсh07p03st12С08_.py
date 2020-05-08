n = int(input())
# n = 3
sum1 = 0
sum2 = 0
for i in range(1, n + 1):
    # print("i = ", i)
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i
if sum1 == 0:
    print(sum2)
else:
    print(sum2 - sum1)
