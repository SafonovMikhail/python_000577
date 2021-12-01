'''
Сломанный мост [91]

task_0091_codechick_bridge_d20211119.py

[Валидация, Основы языка, Строки, Легко]

Напишите функцию, которая проверяет, безопасно ли идти по мосту.
На вход подается строка, состоящая из # и пробелов (дырок в мосте).
Нужно проверить, нет ли в мосту отверстий, в которые можно провалиться.
Если дырок нет, выведите True, иначе выведите False.

Примеры
is_safe_bridge("####") ➞ True
is_safe_bridge("## ####") ➞ False
is_safe_bridge("#") ➞ True

'''


def is_safe_bridge(s):
    flag = True
    for i in s:
        if i == ' ':
            flag = False
            return flag
    return flag


print(is_safe_bridge("####"))
print(is_safe_bridge("## ##"))
print(is_safe_bridge("#"))
