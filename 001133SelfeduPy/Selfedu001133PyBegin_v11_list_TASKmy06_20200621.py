'''
обратить случайно сгенерированное стозначное число
подсказка: Selfedu001133PyBegin_v11_list_02_numDivList_20200416.py
'''
import random

num1 = int((random.random()) * 1e100)
print(num1)
list1 = []
while num1:
    list1.append(str(num1 % 10))
    num1 = num1 // 10
# print(list1)
list1 = ''.join(list1)
print(int(list1))
# print(int(list1) * 10) # проверка на "числовость" вопрос!!!
