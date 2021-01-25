'''
Решите уравнение в натуральных числах
28n + 30 k + 31 m = 365
'''
count = 0
for m in range(1, 12):
    for k in range(1, 13):
        for n in range(1, 12):
            if 28*n+30*k +31*m == 365:
                print(f"31days:{m}, 30days:{k}, 28days:{n}")
                count += 1
print(count)