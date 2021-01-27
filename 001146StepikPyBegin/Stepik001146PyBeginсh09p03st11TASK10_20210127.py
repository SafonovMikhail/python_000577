str1 = input()
# str1 = 'gggggggg1212321ABDCEFCE'
# str1 = 'abcABCD12345'
str1Upper = str1.upper()
# strABC='gggggggg1212321ABDCEFCE'
count = 0
for i in range(len(str1)):
    if str1[i] != str1Upper[i]:
        # print(str1[i])
        count += 1
print(count)

'''
Нижний регистр
На вход программе подается строка. Напишите программу, которая подсчитывает
количество буквенных символов в нижнем регистре.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести количество буквенных символов в нижнем регистре.

Sample Input 1:

abcABCD12345
Sample Output 1:

3
Sample Input 2:

gggggggg1212321ABDCEFCE
Sample Output 2:

8
Sample Input 3:

2376423745dhdhdPPPP
Sample Output 3:

5
'''
