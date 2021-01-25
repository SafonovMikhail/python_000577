str1 = input()
# str1 = '8'
decStr = ''
decStrRev = ''
while int(str1) > 0:
    if int(str1) % 2 == 0:
        decStr += '0'
    else:
        decStr += '1'
    str1 = int(str1) // 2
    str1 = str(str1)
for i in range(-1, -(len(decStr) + 1), -1):
    decStrRev += decStr[i]
# print(decStr)
print(int(decStrRev))

'''
Decimal to Binary
На вход программе подается натуральное число, записанное в десятичной
системе счисления. Напишите программу, которая переводит данное число
в двоичную систему счисления.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести число записанное в двоичной системе счисления.

Sample Input 1:

5
Sample Output 1:

101
Sample Input 2:

128
Sample Output 2:

10000000
'''
