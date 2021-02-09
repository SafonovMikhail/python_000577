'''
Stepik001146PyBeginсh11p04st05TASK04_20210204_lists_methods.py

Без дубликатов
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.

Sample Input:

5
first
second
first
third
second
Sample Output:

first
second
third
'''
n = int(input())
wlist = []
wlist.append(input())
for i in range(n - 1):
    new_item = input()
    wlist.append(new_item)
    for j in range(len(wlist) - 1):
        if wlist[j] == new_item:
            del wlist[-1]
for i in wlist:
    print(i)
