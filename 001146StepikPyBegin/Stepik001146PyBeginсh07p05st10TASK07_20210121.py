num = int(input())
# num = 21111
# num = 11111
# num = 221222
condition = 'NO'
lastNum = 0
preLastNum = 0
while len(str(num)) != 1:
    num1 = num % 10
    num2 = (num % 100) // 10
    lastNum = num1
    preLastNum = num2
    if (lastNum == preLastNum) or (lastNum < preLastNum):
        condition = 'YES'
    else:
        condition = 'NO'
        break
    num //= 10
if len(str(num)) == 1:
    condition = 'YES'
print(condition)



'''
Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию и «NO» в противном случае.

Sample Input 1:

5321
Sample Output 1:

YES
Sample Input 2:

7820
Sample Output 2:

NO
'''