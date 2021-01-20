'''



'''


num1 = int(input())
# num1 = 123456
max1 = -1
min1 = 10
# print(num1)
while num1 != 0:
    num2 = num1 % 10
    # print(num2)
    if min1 > num2:
        min1 = num2
    # print("min1: ", min1)
    if max1 < num2:
        max1 = num2
    # print("max1: ", max1)
    num1 = num1 // 10
print("Максимальная цифра равна", max1)
print("Минимальная цифра равна", min1)
