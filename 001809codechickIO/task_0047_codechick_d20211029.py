'''
Строка пустая?

[Валидация, Основы языка, Строки, Легко]

Напишите функцию, которая возвращает True, если строка — пустая, и False в противном случае.

Примеры:
is_empty("") ➞ True
is_empty(" ") ➞ False
is_empty("a") ➞ False

Примечание:
Строки, которые содержат только пробелы " " не считаются пустым.
Не забудьте вернуть return.
'''


def is_empty(string):
    if string == '':
        flag = True
    else:
        flag = False
    return flag


my_str = ''
print(is_empty(my_str))
