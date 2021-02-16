'''
Напиши программу на вход которой подается некоторая строка. Программа должна вывести True в том случае если во введенной строке есть хотя бы одна цифра и False если цифр нет.

Sample Input:

ИТ-класс
Sample Output:

False
'''
s = input()
count1 = 0
for i in s:
    if i.isdigit() == True:
        count1 += 1
        break
if count1 == 1:
    print(True)
else:
    print(False)
