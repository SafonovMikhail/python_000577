'''
Добавь разделитель
На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

Формат входных данных
На вход программе подается строка текста и строка разделитель, каждая на отдельной строке

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

1234567
*
Sample Output 1:

1*2*3*4*5*6*7
Sample Input 2:

qwerty and password
**
Sample Output 2:

q**w**e**r**t**y** **a**n**d** **p**a**s**s**w**o**r**d
'''
# s = input()
s = 'qwerty andpassword'
# join1 = input()
join1 = '***'
s1 = list()
for i in s:
    s1.append(i)
# print(s1)
s2 = join1.join(s1)
print('var1:')
print(s2)
print('var2:')
print(s, sep=join1)  # в задачи!
print('var3:')
# print(*input(), sep=input())
print(*s, sep=join1) # что делает звездочка?

