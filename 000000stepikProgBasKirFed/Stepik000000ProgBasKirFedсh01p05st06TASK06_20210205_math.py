'''
На вход программе подается натуральное трехзначное число. Напишите программу, которая выводит сначала количество сотен в этом числе, затем количество десятков в этом числе и затем количество единиц в этом числе. Другими словами, напишите программу, которая выводит цифры трехзначного числа через пробел.

Sample Input 1:

123
Sample Output 1:

1 2 3
Sample Input 2:

379
Sample Output 2:

3 7 9
'''
n = int(input())
print(n // 100, n % 100 // 10, n % 10)
