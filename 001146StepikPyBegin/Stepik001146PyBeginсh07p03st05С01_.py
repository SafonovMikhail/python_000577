a = int(input())
b = int(input()) + 1
count = 0
for i in range(a, b):
    if ((i ** 3) % 10 == 4) or ((i ** 3) % 10 == 9):
        count += 1
print(count)