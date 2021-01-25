str1 = input()
# str1 = 'aabbcc'
# str1 = 'abcd'
# str1 = 'aaa'
countDouble = 0
for i in range(0, len(str1) - 1):
    if str1[i] == str1[i + 1]:
        countDouble += 1
        continue
print(f'Парный символ встречается {countDouble} раз')
'''
Одинаковые соседи
На вход программе подается одна строка. Напишите программу,
которая определяет сколько в ней одинаковых соседних символов.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество одинаковых соседних символов.

Sample Input 1:

abcd
Sample Output 1:

0
Sample Input 2:

aabbcc
Sample Output 2:

3
Sample Input 3:

aaa
Sample Output 3:

2
'''
