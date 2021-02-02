# зададим список
numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
info = ['Timur', 1992, 61.5]
num_of_nums = [numbers, languages, info]
for i in num_of_nums:
    print(i)
print()

mylist1 = []  # пустой список
mylist2 = list()  # пустой список
print()

print('Вывод списка:')
print(numbers)
print(languages)
print()

print('функция list()')
numbers = list(range(5))
print(numbers)
print()

even_numbers = list(range(0, 10, 2))  # список содержит четные числа 0, 2, 4, 6, 8
odd_numbers = list(range(1, 10, 2))  # список содержит нечетные числа 1, 3, 5, 7, 9
print(even_numbers, odd_numbers)
print()

s = 'abcde'
chars = list(s)  # список содержит символы 'a', 'b', 'c', 'd', 'e'
print(chars)
print()






