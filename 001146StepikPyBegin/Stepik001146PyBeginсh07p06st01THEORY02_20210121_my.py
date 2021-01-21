'''
Напишем программу, использующую цикл for, которая считывает 10 чисел и суммирует их до тех пор, пока не обнаружит отрицательное число
'''
result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)
