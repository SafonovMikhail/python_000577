# num = input()
num = '375292003040' # ввод именно в виде строковой переменной, иначе, сработает приведение типов
if len(num) >= 8 and num.isdigit():
    print('*'*len(num[:-4]) + num[-4:])
else:
    print('Ошибка')
