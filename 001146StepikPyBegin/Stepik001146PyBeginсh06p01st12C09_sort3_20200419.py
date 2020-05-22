nums = int(input())
num2 = int(input())
num3 = int(input())

max3 = num1
if num1 < num2:
    max3 = num2
if num2 < num3:
    max3 = num3
print(max3)
min3 = num1
if num1 > num2:
    min3 = num2
if num2 > num3:
    min3 = num3
