'''
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

Sample Input 1:

12345
Sample Output 1:

15
Sample Input 2:

12
Sample Output 2:

3
Sample Input 3:

7
Sample Output 3:

7

заготовка:
# объявление функции
def print_digit_sum(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
'''


# объявление функции
def print_digit_sum(num):
    sum1 = 0
    for i in str(n):
        sum1 += int(i)
    print(sum1)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
print()


# -------------------------------------------

# Fan S
# https://stepik.org/lesson/333525/step/10?discussion=1614209&thread=solutions&unit=316953

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))


n = int(input())

print_digit_sum(n)
print()


# -------------------------------------------
# Мария Козеева
# https://stepik.org/lesson/333525/step/10?discussion=1768250&thread=solutions&unit=316953

# объявление функции
def print_digit_sum(n):
    c = 0
    while n != 0:
        b = n % 10
        c += b
        n = n // 10
    print(c)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
print()

# upd: c += n  % 10

# -------------------------------------------
# Константин
# https://stepik.org/lesson/333525/step/10?discussion=1814446&thread=solutions&unit=316953

def print_digit_sum(num):
    print(sum([int(i) for i in num]))
print_digit_sum(input())
print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------

print()

# -------------------------------------------
