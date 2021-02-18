'''
Улитка ползет по вертикальному шесту высотой h метров,
поднимаясь за день на a метров, а за ночь спускаясь на b метров.
На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число.
Гарантируется, что a>b.
'''
import math

h_height = int(input())
# h_height = 10
a_day = int(input())
# a_day = 3
b_night = int(input())
# b_night = 2
h_snail = 0
count = 0
while h_height >= h_snail:
    h_snail += a_day
    if h_height >= h_snail:
        count += 1
    if h_height < h_snail:
        break
    h_snail -= b_night
print(count)

# print((h_height - a_day) // (a_day - b_night) + math.ceil(h_height % a_day))
