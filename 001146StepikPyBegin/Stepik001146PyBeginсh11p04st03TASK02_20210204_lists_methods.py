'''
Значение функции
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая для каждого введенного числа x
выводит значение функции f(x) = x^2 + 2x + 1, каждое на отдельной строке.

Формат входных данных
На вход программе подаются натуральное число n, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку,
а затем соответствующие значения функции.

Примечание. Для первого теста имеем:
... см.
Stepik001146PyBeginсh11p04st03TASK02_20210204_lists_methods_03.jpg
Stepik001146PyBeginсh11p04st03TASK02_20210204_lists_methods_02.jpg
Stepik001146PyBeginсh11p04st03TASK02_20210204_lists_methods_01.jpg

Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

1
2
3
4
5

4
9
16
25
36
Sample Input 2:

3
10
20
30
Sample Output 2:

10
20
30

121
441
961

'''
num1 = int(input())  # вводим натуральное число (количество элементов в списке)
list_num = []  # создаем пустой список
list_symb = []
for i in range(num1):
    list_num.append(int(input()))  # заполняем список (append)
for i in list_num:
    print(i)
print()
for i in range(num1):
    item1 = list_num[i]
    list_symb.append(item1 ** 2 + 2 * item1 + 1)  # заполняем список (append)
    print(list_symb[i])

