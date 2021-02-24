'''
Задача «Отрицательная степень»
Условие
Дано действительное положительное число a и целоe число n.

Вычислите a^n. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
'''


def power(a, n):
    res = 1
    n1 = abs(n)
    if n > 0:
        for i in range(1, int(n1) + 1):
            res *= a
        return res
    else:
        for i in range(1, int(n1) + 1):
            res *= 1 / a
        return res


a = float(input())
n = float(input())
print(power(a, n))


# Решение разработчиков
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input()), int(input())))
