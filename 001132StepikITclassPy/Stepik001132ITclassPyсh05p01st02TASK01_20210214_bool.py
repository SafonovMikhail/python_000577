'''
Напиши программу, которая выводит True, тогда, когда пользователь ввел не пустую строку, и False в случае пустой строки.

Sample Input 1:

привет
Sample Output 1:

True
Sample Input 2:


Sample Output 2:

False
Sample Input 3:

0
Sample Output 3:

True
'''
s = input()
if s == '':
    print(False)
else:
    print(True)
