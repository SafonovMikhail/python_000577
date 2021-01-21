# num1 = int(input())
num1 = 439
prime = 'YES'
for i in range(2, (num1-1)):
    if num1 % i == 0:
        prime = 'NO'
        break
    else:
        prime = 'YES'
print(f'prime: {prime}')

'''
проверка, является ли число простым'''