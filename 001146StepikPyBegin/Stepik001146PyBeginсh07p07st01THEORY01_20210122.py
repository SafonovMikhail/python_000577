'''
оптимизация кода - нахождение простого числа
'''
# перебираем все числа
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# до num//2 +1
num = int(input())
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# не превосходит квадратного корня из этого числа
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

