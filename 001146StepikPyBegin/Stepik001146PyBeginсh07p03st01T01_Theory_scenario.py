counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больших 10.')

# несколько счетчиков. Модифицируем предыдущую программу:
# посчитаем еще и количество нулей среди введенных чисел.
counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.')

# суммирование чисел, бОльших 10
total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна', total)

# нахождение среднего значения
total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)

# обмен значеними переменных





