'''

Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести число записанное в обратном порядке.

Sample Input 1:

5086334
Sample Output 1:

4336805

'''

# num1 = int(input())
num1 = 12345
while num1 != 0:
    print(num1 % 10, end="")
    num1 = num1 // 10
