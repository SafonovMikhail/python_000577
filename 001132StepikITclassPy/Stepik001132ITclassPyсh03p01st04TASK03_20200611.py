'''
Напиши программу, которая принимает на вход два целых числа, а на выходе
печатает результат деления первого числа на второе, с точностью до пяти знаков после запятой.
Stepik001132ITclassPyсh03p01st04TASK03_20200611.py

'''
num1 = float(input())
num2 = float(input())
num3 = num1 / num2
print(f'{num3: .{5}f}')
