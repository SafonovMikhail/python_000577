'''
Напишите программу, которая упорядочивает три числа от большего к меньшему.
'''

list1 = [int(input()), int(input()), int(input())]
list2 = sorted(list1, reverse=True)
print(list2[0])
print(list2[1])
print(list2[2])
