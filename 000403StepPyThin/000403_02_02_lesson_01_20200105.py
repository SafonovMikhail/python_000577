'''
пример в лекции:
ввод двух значений осуществляется через пробел
программа завершается после 5-ти последовательных вводов
'''
i = 0
while i <= 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a * b)
    i += 1
