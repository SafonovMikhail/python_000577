'''
Список строк
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает из указанных строк список и выводит его.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из указанных строк.

Sample Input:

5
C#
C++
C
Python
F#
Sample Output:

['C#', 'C++', 'C', 'Python', 'F#']
'''
numStr = int(input())
list1 = [0]
newList = list1 * numStr
# newList = []
# print(newList)
i = 0
while i < numStr:
    listItem = input()
    newList[i] = listItem
    i += 1
print(newList)
