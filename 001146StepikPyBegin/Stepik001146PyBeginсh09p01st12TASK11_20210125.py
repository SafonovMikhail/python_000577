str1 = input()
# str1 = 'bcd+a++++**31415'
countPlus = 0
countStar = 0
for i in str1:
    if i=='*':
        countStar+=1
    if i=='+':
        countPlus+=1
print(f'Символ + встречается {countPlus} раз')
print(f'Символ * встречается {countStar} раз')

'''
Сколько раз?
На вход программе подается одна строка. Напишите программу, 
которая определяет сколько раз в строке встречаются символы + и *.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести сколько раз встречаются символы  + и * в строке.

Sample Input:

bcd+a++++**31415
Sample Output:

Символ + встречается 5 раз
Символ * встречается 2 раз
'''