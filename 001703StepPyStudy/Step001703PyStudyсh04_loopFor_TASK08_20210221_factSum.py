'''
Задача «Сумма факториалов»
Условие
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.
'''
n = int(input())
sum1 = 0
fact1 = 1
for i in range(1, n + 1):
    fact1 *= i
    sum1 += fact1
print(sum1)
