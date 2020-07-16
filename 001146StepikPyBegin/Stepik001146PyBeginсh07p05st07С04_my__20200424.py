# num1 = int(input())
num1 = 123456
print('num1 :', num1)
print('str(num1) :', str(num1))
num4 = str(num1)
print('num4 :', num4)
# сумма всех цифр
sum1 = 0

# количетво цифр
countDigits = 0

# произведение
prod1 = 1

sum2 = 0

while num1 != 0:  # пока в числе есть цифры
    num2 = num1 % 10  #
    print("num1: ", num1)
    countDigits += 1
    # print("last num: ", num2)
    sum1 += num2
    prod1 *= num2
    num1 = num1 // 10

num3 = str(num1)
print('num3 :', num3)

for i in num4:
    print(i)
    sum2 += int(i)

print("sum1: ", sum1)
print("countDigits: ", countDigits)
print("prod1: ", prod1)  # Факториал
print("aver: ", sum1 / countDigits)
print("sum2: ", sum2)
