'''
AND, OR и NOT [77]

task_0077_codechick_andOrNot_d20211115.py


Логика
Условия
Легко
Реализуйте 3 логические функции: AND (И), OR (ИЛИ) и NOT (НЕ).

Примеры
AND(1, 1) ➞ 1
AND(0, 0) ➞ 0

OR(1, 0) ➞ 1
OR(1, 1) ➞ 1

NOT(0) ➞ 1
NOT(1) ➞ 0

'''


def NOT(num):
    if num == 1:
        return 0
    else:
        return 1


def AND(num, num2):
    if num == num2 and num != 0:
        return 1
    else:
        return 0


def OR(num, num2):
    if num != num2:
        return 1
    if num == num2 and num == 1:
        return 1
    else:
        return 0


print(AND(1, 1))
print(AND(0, 0))

print(OR(1, 0))
print(OR(1, 1))

print(NOT(0))
print(NOT(1))
