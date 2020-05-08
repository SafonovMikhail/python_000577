n = int(input())
fact1 = 1
if n <= 12:
    for i in range(1, n + 1):
        fact1 *= i
print(fact1)
