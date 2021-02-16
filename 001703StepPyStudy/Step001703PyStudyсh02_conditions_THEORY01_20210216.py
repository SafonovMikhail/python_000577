# 1. Синтаксис условной инструкции
# x = int(input())
x = -1
if x > 0:
    print(x)
else:
    print(-x)

# неполное ветвление

# x = int(input())
x = 10
if x < 0:
    x = -x
print(x)

# 2. Вложенные условные инструкции
# x = int(input())
x = 10
# y = int(input())
y = -1
if x > 0:
    if y > 0:  # x > 0, y > 0
        print("Первая четверть")
    else:  # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y > 0:  # x < 0, y > 0
        print("Вторая четверть")
    else:  # x < 0, y < 0
        print("Третья четверть")

# 3. Операторы сравнения


# 4. Тип данных bool
# Пример. Проверим, что хотя бы одно из чисел a или b оканчивается на 0:
# a = int(input())
# b = int(input())
a = 10
b = 11
if a % 10 == 0 or b % 10 == 0:
    print('YES')
else:
    print('NO')

# 5. Каскадные условные инструкции
# определить четверть координатной плоскости
# x = int(input())
# y = int(input())
x = -1
y = -2
if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif y > 0:
    print("Вторая четверть")
else:
    print("Третья четверть")
