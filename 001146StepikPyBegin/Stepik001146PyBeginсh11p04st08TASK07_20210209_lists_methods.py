'''
Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число n, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

7
3
-4
1
0
-1
0
-2
Sample Output 1:

-4
-1
-2
0
0
3
1
Sample Input 2:

5
4
3
-2
-10
0
Sample Output 2:

-2
-10
0
4
3
'''
n = int(input())
list_pos = []
list_zeros = []
list_negs = []
list_of_lists = []
for i in range(n):
    num = int(input())
    if num > 0:
        list_pos.append(num)
    if num == 0:
        list_zeros.append(num)
    if num < 0:
        list_negs.append(num)
# print(list_pos)
# print(list_zeros)
# print(list_pos)
list_of_lists.extend(list_negs)
list_of_lists.extend(list_zeros)
list_of_lists.extend(list_pos)
# print(list_of_lists)
for i in list_of_lists:
    print(i)
