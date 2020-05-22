num1 = int(input())
# сумма всех цифр
sum1 = 0
# количетво цифр
countDigits = 0

while num1 != 0: # пока в числе есть цифры
    num2 = num1 % 10 #
    print(num1)
    countDigits += 1
    print("last num: ", num2)
    sum1 += num2
    num1 = num1 // 10

print("sum1:", sum1)
print("countDigits:", countDigits)
