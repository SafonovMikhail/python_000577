num = input()
# num = 375292003040
if len(str(num)) >= 8 and num.isdigit():
    print('*'*len(num[:-4]) + num[-4:])
else:
    print('Ошибка')
