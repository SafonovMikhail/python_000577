# dig = input("Введите число: ")
dig = '1234'
if (dig.isdigit()):
    dig = int(dig)
    print(dig)
else:
    print("Число введено неверно")

str = "HW"
print(str.rjust(10, "$"))
print(str.ljust(10, "$"))
