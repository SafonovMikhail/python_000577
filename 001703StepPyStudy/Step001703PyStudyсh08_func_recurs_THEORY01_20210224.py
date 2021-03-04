print()
# ----------------------------
print('1. Функции')
# факториал
# вычислим 3!
res = 1
for i in range(1, 4):
    res *= i
print(res)

# вычислим 5!
res = 1
for i in range(1, 6):
    res *= i
print(res)
print()

# ----------------------------
print('# функция "факториал"')


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(3))
print(factorial(5))
print()

# ----------------------------
print('# функция "max"')


def max(a, b):
    if a > b:
        return a
    else:
        return b


print(max(3, 5))
print(max(5, 3))
# print(max(int(input()), int(input())))
print()

# ----------------------------
print('# функция "max3"')


def max1(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max1(max1(a, b), c)


print('max3:', max3(3, 5, 4))
print()

# ----------------------------
print('def max(*a):')


def max4(*a):  # формируется кортеж из произвольного количества переменных
    res = a[0]
    for val in a[1:]:  # перебираем значения кортежа
        if val > res:
            res = val
    return res


print(max4(3, 5, 4))
print(max4(3, 5, 4, 5, 6, 7, 8, 9))
print(max4(3, 5, 4, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 16, 70))
print()

######## 2. Локальные и глобальные переменные ########
# ----------------------------
print('# 2. Локальные и глобальные переменные')


def f():
    print(a)


a = 1  # переменная объявляется вне функции
f()
print()

# ----------------------------
print('Локальные и глобальные переменные [02]')


def f():
    a1 = 1
    print("a1(локальная переменная, объявленная внутри функции):",a1)


a1 = 11
f()
print('a1(после вызова функции с одноименной переменной): ',a1)
print(f"значение глобальной переменной a1:{a1} остается неизменным")

print()

# ----------------------------
print('# пример (факториал)')


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')
print()

# ----------------------------
print('global')


def f():
    global a
    a = 1
    print(a)


a = 0
f()
print("вне функции: ", a)

print()

# ----------------------------
print('# факториал вводимого числа')


# начало куска кода, который можно копировать из программы в программу
def factorial1(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


# конец куска кода

# n = int(input())
n = 5
m = 6
f1 = factorial1(m) - factorial1(n)
print(len(str(factorial1(m))), factorial1(m))
print(len(str(factorial1(n))), factorial1(n))
print(len(str(f1)), f1)
# дальше всякие действия с переменной f
print()

# ----------------------------
print('# 3. Рекурсия')


def short_story(count):
    print(f"{~ count + 1}" " У попа была собака, он ее любил.")
    print("Она съела кусок мяса, он ее убил,")
    print("В землю закопал и надпись написал:")
    count += 1
    if count <= 20:
        short_story(count)


short_story(0)

print()

# ----------------------------
print('# индексы (отрицательные)')


def factorial5(n):
    if n == 0:
        return 1
    else:
        return n * factorial5(n - 1)


print(factorial5(5))
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
print()

# ----------------------------
print('# индексы (отрицательные)')
