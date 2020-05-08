sum = 0;
i = 1
while i <= 1000:
    sum += 1 / i
    i += 1
print(sum)

sum = 0
i = 1
while i <= 1000 and sum < 5:
    sum += 1 / i
    i += 1
print("sum: \t", sum)
print("i: \t\t", i)
