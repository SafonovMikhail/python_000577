'''
На вход программе подается два целых числа. Напишите программу, которая выводит разницу их произведения с их суммой.

Sample Input 1:

3
4
Sample Output 1:

5
Sample Input 2:

10
15
Sample Output 2:

125
'''
n1, n2 = int(input()), int(input())
print(n1 * n2 - (n1 + n2))
