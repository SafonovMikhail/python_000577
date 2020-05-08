num1 = int(input()) + 1
sum1 = 0
sum2 = 0
for i in range(num1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        sum1 += i
sum2 = sum1
print(sum2)
