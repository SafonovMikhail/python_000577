# a = int(input())
a = 123456
sumLeft = a % 100000
sumRright = a // 100000 + a // 10000
print(sumRright)
print(sumLeft)

if sumLeft == sumRright:
    print("Счастливый")
else:
    print("Обычный")
