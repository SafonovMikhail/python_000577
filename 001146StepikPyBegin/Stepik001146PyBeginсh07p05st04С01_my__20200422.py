'''

Что покажет приведенный ниже фрагмент кода?

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)

'''


num1 = 12345
while num1 != 0:
    print(num1 % 10)
    num1 = num1 // 10
