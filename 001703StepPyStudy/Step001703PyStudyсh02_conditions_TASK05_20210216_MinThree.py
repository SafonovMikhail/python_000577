'''
Даны три целых числа. Выведите значение наименьшего из них.
'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
min1 = n1
if n2 < min1:
    min1 = n2
if n3 < min1:
    min1 = n3
print(min1)
