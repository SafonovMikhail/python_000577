print()

# ----------------------------
print('# 6. Срезы (slices)')
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
print()

# ----------------------------
print('# Определить количество цифр натурального числа')
# n = int(input())
n = 100
length = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    length += 1
print(length)
print()

# ----------------------------
print('# выполнение блока [else]')
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Цикл окончен, i =', i)
print()

# ----------------------------
print('# break')
a = int(input())
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input())
else:
    print('Ни одного отрицательного числа не встретилось')
print()

# ----------------------------
print('# loop for, break')
n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
else:
    print('Ни одного отрицательного числа не встретилось')
print()

# ----------------------------
print('# выполнение блока [break]')
for i in range(3):
    for j in range(5):
        if j > i:
            break
        print(i, j)
print()
# ----------------------------
print('# плохое использование [break]')
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break  # плохое использование
print('Длина числа равна', length)
print()
# ----------------------------
print('# лучшее решение')
n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Длина числа равна', length)
print()
# ----------------------------
print('# решение на питоне')
n = int(input())
print('Длина числа равна', len(str(n)))
print()
# ----------------------------
print('# Множественное присваивание')
a, b = 0, 1
a1 = 0
b1 = 1

print()
# ----------------------------
print('#  обменять значения двух переменных')
a2 = 1
b2 = 2
a2, b2 = b2, a2
print(a, b)

print()
# ----------------------------
print('# 2. Срезы (slices)')

print()
# ----------------------------
print('# 2. Срезы (slices)')

print()
# ----------------------------
print('# 2. Срезы (slices)')

print()
