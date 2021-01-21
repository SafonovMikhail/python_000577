'''
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
---

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
---

Sample Input 1:
5678

Sample Output 1:

26
4
1680
6.5
5
13

'''

num = input()
# num = '5678'
lenNum = len(num)
num = int(num)
sum1 = 0
comp1 = 1
aver1 = 0
fNum = num // (10**(lenNum-1))
lNum = num % 10
sum_fl_num = fNum + lNum
while num != 0:
    num1 = num % 10
    sum1 += num1
    comp1 *= num1
    num = num // 10

print(sum1)
print(lenNum)
print(comp1)
print(sum1 / lenNum)
print(fNum)
print(sum_fl_num)
