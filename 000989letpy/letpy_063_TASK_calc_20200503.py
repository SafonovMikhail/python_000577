# python_20200503_063_str.py
a = input()
b = input()
if a.isdigit() and b.isdigit():
    print('Сумма=', int(a) + int(b))
else:
    print('Вы ввели не число')
