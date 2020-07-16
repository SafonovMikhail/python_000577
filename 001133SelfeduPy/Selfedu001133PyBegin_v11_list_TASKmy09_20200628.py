## -*- coding: windows-1251 -*-
'''
Selfedu001133PyBegin_v11_list_TASKmy09_20200628.py
список из квадратов натуральных чисел
'''
list = []  # объявление массива
N = 10  # число элментов массива
list = [x ** 2 for x in range(N)]
print(list)