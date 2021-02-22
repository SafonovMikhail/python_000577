'''
Все сразу 2 🌶️
Дополните приведенный код, чтобы он:

Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print().
---
numbers = [8, 9, 10, 11]

'''
numbers = [8, 9, 10, 11]
numbers.insert(1, 17)
numbers.pop(2)
numbers2 = [4, 5, 6]
numbers.extend(numbers2)
numbers.pop(0)
# print(numbers)
numbers.extend(numbers)
# print(numbers)
numbers.insert(3, 25)
print(numbers)

# v.01
# https://stepik.org/lesson/324754/step/5?discussion=1720782&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]

numbers[1] = 17  # !!! дополнить
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# v.02
# https://stepik.org/lesson/324754/step/5?discussion=1633537&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]
numbers[1] = 17  # 1
numbers.extend([4, 5, 6])  # 2
del numbers[0]  # 3
numbers *= 2  # 4 (!!!) интересно
numbers.insert(3, 25)  # 5
print(numbers)  # 6

# v.03
# https://stepik.org/lesson/324754/step/5?discussion=1684867&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]
numbers.remove(numbers[1])
numbers.insert(1, 17)
numbers.extend('456')
numbers = [int(i) for i in numbers]  # ???
numbers.remove(numbers[0])
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)

# v.04
# https://stepik.org/lesson/324754/step/5?discussion=3028692&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend(range(4, 7))
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# v.05
# https://stepik.org/lesson/324754/step/5?discussion=3470215&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]

numbers.insert(1, 17)
del numbers[2]
numbers.insert(-1, 4)
numbers.insert(-1, 5)
numbers.insert(-1, 6)
del numbers[-1]
numbers.insert(-3, 11)
del numbers[0]
numbers = numbers + numbers
numbers.insert(3, 25)
print(numbers)

# v.06
# https://stepik.org/lesson/324754/step/5?discussion=3450945&thread=solutions&unit=307930
numbers = [8, 9, 10, 11]
numbers.pop(1)
numbers.insert(1, 17)
a, b = -1, 4  # для чего 'a'???
for i in range(1, 4):
    numbers.insert(len(numbers), b)
    b += 1
numbers.pop(0)
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)

# v.07
# https://stepik.org/lesson/324754/step/5?discussion=3439992&thread=solutions&unit=307930
# минимальное количество знаков?
l = [8, 9, 10, 11]
l[1] = 17
l += [4, 5, 6]
del l[0]
l *= 2
l.insert(3, 25)
print(l)




# v.01
#


# v.01
#


# v.01
#


# v.01
#


# v.01
#


# v.01
#


# v.01
#
