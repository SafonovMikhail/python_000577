num = int(input())
num1 = num // 1000
num2 = (num // 100) % 10
num3 = (num // 10) % 10
num4 = num % 10
# print(num1)
# print(num2)
# print(num3)
# print(num4)
if num1 + num4 == num2 - num3:
    print("ДА")
else:
    print("НЕТ")
