import math

n = int(input())
# print(math.log(n))
sum1 = 0
for i in range(1, n + 1):
    sum1 += 1 / i
#     print(sum1)
# print(sum1)
print(sum1 - math.log(n))
