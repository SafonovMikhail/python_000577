
'''
На вход программе подается два натуральных числа a и b (a< b). Напишите программу,
которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом:
число с максимальной суммой делителей и сумму его делителей.

Примечание. Если таких чисел несколько, то выведите наибольшее из них.

Sample Input 1:

1
10
Sample Output 1:

10 18
Sample Input 2:

1
100
Sample Output 2:

96 252
'''

a = int(input())
# a = 2
b = int(input())
# b = 6
count_max = 0
sum_max = 0
num_max = 0
for i in range(a, b + 1):
    # print(f"num: {i}, ", end="")
    count = 0
    sum = 0
    for j in range(1, b + 1):
        if i >= j:
            if i % j == 0:
                count += 1
                sum += j
                if sum >= sum_max:
                    sum_max = sum
                    num_max = i
        else:
            continue
# print(f"num: {num_max}, ", end="")
# print(f"sum: {sum_max} ", end="")
print(f"{num_max} {sum_max}")
