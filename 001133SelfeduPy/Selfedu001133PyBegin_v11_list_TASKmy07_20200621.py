'''
список из квадратов четных чисел
Selfedu001133PyBegin_v11_list_TASKmy07_20200621.py
'''
list = []  # объ€вление массива
N = 10  # число элментов массива
list = [x ** 2 for x in range(N) if x % 2 == 0] # квадраты четных чисел
print(list)