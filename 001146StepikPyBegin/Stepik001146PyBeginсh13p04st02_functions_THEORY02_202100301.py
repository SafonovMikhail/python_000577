# ----------------------------
print('# Решение задач')
print(
    '# Задача 1. Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов.')


def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


print(compute_hypotenuse(3, 4))
print(compute_hypotenuse(5, 12))
print(compute_hypotenuse(1, 1))
print()

# ----------------------------
print('# Задача 2. Напишите функцию, вычисляющую расстояние между двумя точками')


def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)


x1, y1 = float(input()), float(input())  # считываем координаты первой точки
x2, y2 = float(input()), float(input())  # считываем координаты второй точки

print(get_distance(x1, y1, x2, y2))  # вычисляем и выводим расстояние между точками
print()

# ----------------------------
print('# Задача 3. Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую сумму его цифр.')


def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result


n = int(input())
print(sum_digits(n))  # вычисляем и выводим сумму цифр считанного числа
print()

# ----------------------------
print(
    '# Задача 4. Напишите функцию, принимающую в качестве аргумента список чисел и возвращающую среднее значение элементов списка.')


def compute_average(numbers):
    return sum(numbers) / len(numbers)


numbers = [1, 3, 5, 1, 6, 8, 10, 2]
print(numbers)
print(compute_average(numbers))  # вычисляем и выводим среднее значение элементов списка
print()

# ----------------------------
print('# ')

print()

