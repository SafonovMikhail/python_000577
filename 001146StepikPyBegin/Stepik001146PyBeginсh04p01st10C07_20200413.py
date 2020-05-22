num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
min = num1
if num1 > num2:
    min = num2
if min > num3:
    min = num3
if min > num4:
    min = num4
print(min)
