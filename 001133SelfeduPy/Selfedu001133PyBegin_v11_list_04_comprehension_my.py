import random

print("Вывод случайного числа при помощи использования random.random()")
rnd = random.random()
print(rnd)
print(rnd * 10000 // 100)
print("random.randint(0,999): ", random.randint(0, 999))
print("random.randrange(0, 999, 2): ", random.randrange(0, 999, 1))

# for x in range(50):
#     print(random.randrange(10, 50, 5))

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Выбор случайного города из списка - ", random.choice(city_list))

list = [55, 66, 77, 88, 99]
print("random.choice используется для выбора случайного элемента из списка - ", random.choice(list))

list = [2, 5, 8, 9, 12]
print("random.sample() ", random.sample(list, 3))

random.seed(1)
print("Случайное число с семенем ", random.random())
print("Случайное число с семенем ", random.random())

random.seed(2)  # не понял назначение числа в скобках
print("Случайное число с семенем ", random.random())
print("Случайное число с семенем ", random.random())

list = [2, 5, 8, 9, 12]
print(list)
random.shuffle(list)  # меняет исходный список! (?)
print("Вывод перемешанного списка ", list)

print("Число с плавающей точкой в пределах заданного промежутка [10.5, 25.5]: ", end='')
print(random.uniform(10.5, 25.5))

print("Число с плавающей точкой через triangular [10.5, 25.5, 5.5]: ", end='')
print(random.triangular(10.5, 25.5, 5.5))

import secrets

# number =
print("Надежное число: ", random.SystemRandom().random())
print("Надежный токен байтов", secrets.token_bytes(16))

number_list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print("Первая выборка ", random.sample(number_list, k=5))
# хранит текущее состояние в объекте state
state = random.getstate()

print("Вторая выборка ", random.sample(number_list, k=5))
# Восстанавливает состояние state, используя setstate
random.setstate(state)

# Теперь будет выведен тот же список второй выборки
print("Третья выборка ", random.sample(number_list, k=5))

# Восстанавливает текущее состояние state
random.setstate(state)
# Вновь будет выведен тот же список второй выборки
print("Четвертая выборка ", random.sample(number_list, k=5))

import numpy

random_float_array = numpy.random.rand(2, 2)
print("2 X 2 массив случайных вещественных чисел в [0.0, 1.0] \n", random_float_array, "\n")
random_float_array = numpy.random.uniform(25.5, 99.5, size=(3, 2))
print("3 X 2 массив случайных вещественных чисел в [25.5, 99.5] \n", random_float_array, "\n")

# random_integer_array = numpy.random.random_integers(1, 10, 5) # deprecated
random_integer_array = numpy.random.randint(1, 10, 5)  # deprecated
print("1-мерный массив случайных целых чисел \n", random_integer_array, "\n")
# random_integer_array = numpy.random.random_integers(1, 10, size=(3, 2)) # deprecated
random_integer_array = numpy.random.randint(1, 10, size=(3, 2))
print("2-мерный массив случайных целых чисел \n", random_integer_array)

array = [10, 20, 30, 40, 50, 20, 40]
print(array)
single_random_choice = numpy.random.choice(array, size=1)
print("один случайный выбор из массива 1-D", single_random_choice)
multiple_random_choice = numpy.random.choice(array, size=3, replace=False)
print("несколько случайных выборов из массива 1-D без замены", multiple_random_choice)
print(array)
multiple_random_choice = numpy.random.choice(array, size=3, replace=True)
print("несколько случайных выборов из массива 1-D с заменой", multiple_random_choice)
# [2020-04-17] что же они тогда заменяют? Массив как был, так и остался.
print(array)

import uuid
# получить уникальный UUID
safeId = uuid.uuid4()
print("безопасный уникальный id: ", safeId)