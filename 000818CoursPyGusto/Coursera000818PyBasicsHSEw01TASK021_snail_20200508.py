h = float(input())
d = int(input())
n = int(input())
x = 0
count = 1
x = x + d
while x < h:
    x = x - n
    x = x + d
    count += 1
print(count)