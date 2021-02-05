'''
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
'''
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
numbers2 = []
for i in range(len(numbers)):
    numbers2.append(numbers[i] ** 2)
print(sum(numbers2))
