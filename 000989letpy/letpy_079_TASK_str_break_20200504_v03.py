'''
letpy_079_TASK_str_break_20200504
Напишите программу, в которой переменной [string] присвоено значение,
введённое пользователем. Тип переменной [string] — строка.
Программа должна вывести каждую букву переменной string на новой строке,
используя цикл [while]. Если в строке встретятся два символа [#] подряд,
цикл должен быть остановлен с помощью оператора [break].
'''
string = input()
# string = '#12345##6789'
# string = '# 123456789#'
# string =  '# 123456789#'
# string = '12345##6789'
# string = '12345#6789'

i = 0
if string.find('##') == (-1):
    while True:
        # if string[i] != "#":
        print(string[i])
        i += 1
        if i == len(string):
            break
else:
    i = 0
    while i < string.find('##'):
        # if string[i] != "#":
        print(string[i])
        i += 1
