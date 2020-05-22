# иллюстрация работы [continue]
S = 0;
i = -5
while i < 4:
    i = i + 1
    if i == 0: continue
    print(i)
    S += 1 / i
print(S)
