print("Доступные команды: \n[+], [-], [*], [/], [%], [**]")
a = float(input())
b = float(input())
i = input()
if (i == '+'):  # попался!!! ввел '=' вместо '=='
    print(a + b)
elif (i == '-'):
    print(a - b)
elif (i == '/'):
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif (i == '*'):
    print(a * b)
elif (i == 'mod'):
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif (i == 'pow'):
    print(a ** b)
elif (i == 'div'):
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
else:
    print('неизвестная функция')
