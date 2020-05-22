n = float(input())
m = float(input())
max = max(n, m)
min = min(n, m)
time = max - min
print(time // 60, time % 60)
