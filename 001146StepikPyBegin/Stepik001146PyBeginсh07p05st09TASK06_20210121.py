num = int(input())
# num = 21111
# num = 221222
sameNums = 'NO'
lastNum = 0
preLastNum = 0
while len(str(num)) != 1:
    num1 = num % 10
    num2 = (num % 100) // 10
    lastNum = num1
    preLastNum = num2
    if lastNum == preLastNum:
        sameNums = 'YES'
    else:
        sameNums = 'NO'
        break
    num //= 10
if len(str(num)) == 1:
    sameNums = 'YES'
print(sameNums)

'''
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

Sample Input 1:

11111
Sample Output 1:

YES
Sample Input 2:

11112111
Sample Output 2:

NO
'''
