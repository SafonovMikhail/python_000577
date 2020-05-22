# Напишем программу, которая считывает
# натуральное число (целое положительное) и обрабатывает
# его цифры.

# n = int(input())
n = 1234567
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа
    print(last_digit)

print("# Определим, есть ли в числе цифра 7.")

# num = int(input())
num = 1234567
has_seven = False  # сигнальная метка
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')
