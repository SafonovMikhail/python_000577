'''
Stepik001132ITclassPyсh02p01st02TASK01_threeNums_20200610.py
Напиши программу, которая на вход получает трехзначное число.
На выходе программа должна печатать три цифры этого числа на разных строках.
'''
num = int(input())
num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10
print(num1)
print(num2)
print(num3)
