'''

Дано натуральное число n. Напишите программу, которая определяет его максимальную и минимальную цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).

Sample Input 1:

26670
Sample Output 1:

Максимальная цифра равна 7
Минимальная цифра равна 0

'''


# num1 = int(input())
num1 = 123456
max1 = -1
min1 = 10
# print(num1)
while num1 != 0:
    num2 = num1 % 10
    # print(num2)
    if min1 > num2:
        min1 = num2
    # print("min1: ", min1)
    if max1 < num2:
        max1 = num2
    # print("max1: ", max1)
    num1 = num1 // 10
print("Максимальная цифра равна", max1)
print("Минимальная цифра равна", min1)
