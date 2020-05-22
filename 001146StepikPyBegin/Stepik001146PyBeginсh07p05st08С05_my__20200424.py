num1 = input()
len1 = len(num1)
num2 = (int(num1) // (10 ** (len1 - 2))) % 10
print(num2)
