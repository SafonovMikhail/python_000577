'''
Напиши программу, которая получает с клавиатуры целое положительное трёхзначное число и записывает в логическую переменную значение True, если это число – палиндром, то есть читается одинаково слева направо и справа налево. После этого на экран выводится ответ на вопрос: «Верно ли, что введённое число – палиндром?».

Sample Input 1:

121
Sample Output 1:

True
Sample Input 2:

123
Sample Output 2:

False
'''
n = input()
if n[0] == n[-1]:
    print(True)
else:
    print(False)
