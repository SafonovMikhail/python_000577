'''
letpy_079_TASK_str_break_20200504
Напишите программу, в которой переменной [string] присвоено значение,
введённое пользователем. Тип переменной [string] — строка.
Программа должна вывести каждую букву переменной string на новой строке,
используя цикл [while]. Если в строке встретятся два символа [#] подряд,
цикл должен быть остановлен с помощью оператора [break].
'''
string = input()
j = 0
while j + 1 < len(string):
    if string[j] == '#' and string[j + 1] == '#':
        break
    elif string[j] != '#':
        print(string[j])
    j += 1
    if j == len(string):
        break

# asdlgkjawig##agkjaslk
# asdlgkjawi#gagkjaslk#
# asdlgkjawigagkjaslk#
