t1 = (4,)
print('t1: ', t1)
print(len(t1))
b = ('1', 2, '4')
print('b: ', b)
t = tuple(range(11))
print(t)
print('t1 + b: ', t1 + b)
t2 = (1, [1, 2], 3)
t2[1][0] = 0 # изменение изменяемого типа!
print(t2)

animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals): # enumerate() функция, которая возвращает индекс и значение для списка
    print (index,value)