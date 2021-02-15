'''
Напиши программу которая проверяет, есть ли во введенной строке, вторая строка. На вход программе дается две строки, на выходе программа выдает True если вторая строка содержится в первой и False в противном случае.

Sample Input:

Школа 1501
1501
Sample Output:

True
'''
s1 = input().split(' ')
s2 = input().split(' ')
count = 0
for i in s1:
    for j in s2:
        if i == j:
            count = +1
            print(True)
            break
if count == 0:
    print(False)
