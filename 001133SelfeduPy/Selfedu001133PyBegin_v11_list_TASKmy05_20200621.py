'''
Selfedu001133PyBegin_v11_list_TASKmy05_20200621.py
разделить прямоугольник горизонтальной линией
согласно образцу
подсказка 1: используйте параметр [sep='']
'''
n = int(input("Количество элементов списка: "))
list1 = []
for i in range(n):
    list1.append(i * '*')
print("задано количество элементов: ", n)

for i in range(len(list1) - 1):
    print(list1[i + 1], list1[n - 1 - i], sep='\\')
