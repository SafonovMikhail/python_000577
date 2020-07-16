'''
не прохоит тесты
'''
h = float(input())
d = int(input())
n = int(input())
x = 0
count = 0
while x < h:
    count += 1
    x = x + 3
    if x < h:
        x = x - 2
print(count)
