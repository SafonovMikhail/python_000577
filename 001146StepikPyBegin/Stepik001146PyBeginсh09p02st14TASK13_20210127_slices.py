str1 = input()
# str1 = 'abcdef'
# str1 = 'abcdefg'
# print(len(str1))
if len(str1) % 2 == 0:
    print(str1[len(str1) // 2:] + str1[:len(str1) // 2])
else:
    print(str1[len(str1) // 2 + 1:] + str1[:len(str1) // 2 + 1])

'''
Две половинки
На вход программе подается строка текста. 
Напишите программу, которая разрежет ее на две равные части, 
переставит их местами и выведет на экран.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.

Sample Input 1:

abcdef
Sample Output 1:

defabc
Sample Input 2:

abcdefg
Sample Output 2:

efgabcd
Sample Input 3:

a
Sample Output 3:

a
'''
