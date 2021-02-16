n1 = input()
if n1.isdigit():
    if 3 <= int(n1) <= 5:
        print('весна')
    if 6 <= int(n1) <= 8:
        print('лето')
    if 9 <= int(n1) <= 11:
        print('осень')
    if 1 <= int(n1) <= 2 or int(n1) == 12:
        print('зима')
    if int(n1) > 12:
        print('нет такого месяца')
else:
    print('нет такого месяца')
