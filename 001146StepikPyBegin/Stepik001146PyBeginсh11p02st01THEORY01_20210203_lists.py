print()
print('функция len():')
numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']

print(len(numbers))  # выводим длину списка numbers
print(len(languages))  # выводим длину списка languages

print(len(['apple', 'banana', 'cherry']))  # выводим длину списка, состоящего из 3 элементов
print()

print('функция in:')
numbers = [2, 4, 6, 8, 10]
if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')
print()

print('функция in (с "not"):')
numbers = [2, 4, 6, 8, 10]
if 0 not in numbers:
    print('Список numbers не содержит нулей')
print()

print('срезы:')
numbers = [2, 4, 6, 8, 10]
print(numbers)
print('numbers[1:3]:', numbers[1:3])
print('numbers[2:5]:', numbers[2:5])
print()

print('срезы: использование для изменения элементов')
fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
print('исходный список:', fruits)
fruits[2:5] = ['банан', 'вишня', 'киви']
print('результирующий список:', fruits)
print()

print('Операция конкатенации + и умножения на число *')
print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)
print()

print('расширенные операторы += и *= при работе со списками')
a = [1, 2, 3, 4]
b = [7, 8]
a += b  # добавляем к списку a список b
b *= 5  # повторяем список b 5 раз
print(a)
print(b)
print()

print('Встроенные функции sum(), min(), max()')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print('sum():', sum(numbers))
print('min():', min(numbers))
print('max():', max(numbers))
numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print()
print(numbers)
print('sum():', sum(numbers))
print('min():', min(numbers))
print('max():', max(numbers))
print()


numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
numbers[1] = 101  # изменяем 2 элемент (по индексу 1) списка
print('изменяем 2 элемент (по индексу 1) списка')
print(numbers)
