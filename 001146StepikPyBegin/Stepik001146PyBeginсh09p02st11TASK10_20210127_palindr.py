str1=input()
# str1 = 'потоп'
# str1 = 'непотоп'
str2 = str1[::-1]
if str1 == str2:
    print('YES')
else:
    print('NO')
print(str1)
print(str2)

'''
На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.

Формат входных данных
На вход программе подается одно слово в нижнем регистре.

Формат выходных данных
Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.

Примечание. Палиндром читается одинаково в обоих направлениях, например слово «потоп».

Sample Input 1:

потоп
Sample Output 1:

YES
Sample Input 2:

анекдот
Sample Output 2:

NO
'''
