'''
Дюймы в футы [89]

task_0089_codechick_feet-Inch_d20211119.py

[Математика, Основы языка, Легко]

Напишите функцию, которая принимает значение длины в дюймах, и конвертирует его в футы.

Примеры
inches_to_feet(324) ➞ 27
inches_to_feet(12) ➞ 1
inches_to_feet(36) ➞ 3

Примечание
В одном футе 12 дюймов.
Если на вход поступает значение меньше 12, верните 0.

'''


def inches_to_feet(inches):
    if inches < 12:
        return 0
    else:
        return inches / 12
