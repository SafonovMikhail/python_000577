'''
Напиши программу, которая получает с клавиатуры целое положительное трёхзначное число и записывает в логическую переменную значение True, если это все его цифры одинаковы. После этого на экран выводится ответ на вопрос: «Верно ли, что все цифры введённого числа одинаковы?»

Sample Input 1:

888
Sample Output 1:

True
Sample Input 2:

112
Sample Output 2:

False
'''
n = input()
if n[0] == n[1] == n[2]:
    print(True)
else:
    print(False)
