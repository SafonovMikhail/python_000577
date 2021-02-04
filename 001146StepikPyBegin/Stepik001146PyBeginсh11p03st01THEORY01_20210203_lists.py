# ---------------------
print()
print('Метод append()')
numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список
print(numbers)
numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка
print(numbers)
print()
# ---------------------
numbers = []  # создаем пустой список
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
print()
# ---------------------
print("Метод extend()")
numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]
print('numbers:', numbers)
print('odds:', odds)
numbers.extend(odds)
print(numbers)
print()
# ---------------------
words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']
words1.append('python')
words2.extend('python')
print(words1)
print(words2)
print()
# ---------------------
print('Удаление элементов')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
del numbers[5]    # удаляем элемент имеющий индекс 5
print(numbers)
print()
# ---------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
del numbers[2:7]    # удаляем элементы с 2 по 6 включительно
print(numbers)
print()
# ---------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
del numbers[::2]
print(numbers)





