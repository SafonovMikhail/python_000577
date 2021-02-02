num_letter = int(input())
# num_letter = 5
list_letter = list(range(97, 97 + num_letter))
# print(list_letter)
list_letter2 = []
for i in range(len(list_letter)):
    list_letter[i] = list_letter2.append(chr(97 + i))
print(list_letter2)

'''
Список букв
На вход программе подается одно число n. 
Напишите программу, которая выводит список, состоящий из 
n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

Формат входных данных
На вход программе подается натуральное число n, n≤26.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

1
Sample Output 1:

['a']
Sample Input 2:

5
Sample Output 2:

['a', 'b', 'c', 'd', 'e']
Sample Input 3:

10
Sample Output 3:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
