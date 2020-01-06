'''
Напишите программу, которая считывает с клавиатуры два числа [a и b],
считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b],
которые делятся на 33.

В приведенном ниже примере среднее арифметическое считается для чисел
на отрезке [-5; 12][−5;12]. Всего чисел, делящихся на 33, на этом о
трезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число,
которое делится на 33.
'''
a, b = (int(i) for i in input().split())
aver = 0
count = 0
while a % 3 != 0:
    a += 1
while b % 3 != 0:
    b -= 1
for i in range(a, b + 1, 3):
    count += 1
    aver += i

print(aver / count)
