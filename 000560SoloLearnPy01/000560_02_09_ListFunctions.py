print("000560_02_09_ListFunctions.py")

print()
print("000560_02_09_ex01_list_append")
# letters[.]append - точка, т.к. это МЕТОД класса списка(list)
letters = ['a', 'b', 'z', ]
print(letters)
print('letters.append(4)')
letters.append(4)
print(letters)

print()
print("000560_02_09_task01_list_append")
#
words = ["Hello"]
print(words)
words.append("world")
print(words)
print(words[1])
# (?)  как записать в одну строку, как предложение:
# вариант: преобразовать в список, вывести его с разделителем в виде пробела?

print()
print("000560_02_09_ex02_list_len")
# len и num - метод, а не функция (перед нужным спиком пишется, точка не ставится)
nums = [1, 2, 3, 4, 5, 6, ]
print('len(nums)')
print(len(nums))

print()
print("000560_02_09_task02_list_len")
#
letters = ['a', 'b', 'c']
print('letters')
print(letters)
print("letters.append('d')")
letters.append('d')
print(letters)
print('len(letters)')
print(len(letters))

print()
print("000560_02_09_ex03_list_insert")
#
words = ['Python', 'fun']
print('words:', words)
print('len(words):', len(words))
print("words.insert('is')")
index = 1
words.insert(index, 'is')
print('len(words):', len(words))
print(words)

print()
print("000560_02_09_task03_list_insert")
#
nums = [9, 8, 7, 6, 5]
print('len(nums):', len(nums))
print(nums)
print('nums.append(4)')
nums.append(4)
print(nums)
print('len(nums):', len(nums))
nums.insert(2, 11)
print('nums.insert(2,11)')
print(nums)
print('len(nums):', len(nums))

print()
print("000560_02_09_ex04_list_INDEX")
#
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z'))  # выдает ошибку, не в списке

print()
print("000560_02_09_task04_list_APPEND_LEN")
#
list = ['a', 'b', 'z', 'a']
print(list)
print('list.append(z)')
list.append('z')
print(list)
print(len(list))

print()
nums = [1, 2, 3, 4]
print(nums)
print("len(nums):", len(nums))
print('nums.append(z)')
nums.append('z')
print(nums)
print("len(nums):", len(nums))

print()
print("000560_02_09_ex05_list_MAX")
#
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print('max(letters):', max(letters))
num = [1, 2, 3, 4, 5, 6]
print()
print(num)
print('max(num):', max(num))

print()
print("000560_02_09_ex06_list_MIN")
#
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print('min(letters):', min(letters))
num = [1, 2, 3, 4, 5, 6]
print()
print(num)
print('min(num):', min(num))

print()
print("000560_02_09_ex07_list_COUNT")
# сколько раз встречается
letters = ['a', 'b', 'z', 'a']
print(letters)
print('letters.count(a):', letters.count('a'))

print()
print("000560_02_09_ex08_list_REMOVE")
#
letters = ['a', 'b', 'z', 'a']
print(letters)
print('letters.remove(z)')
letters.remove('z')
print(letters)

print()
print("000560_02_09_ex09_list_REVERSE")
# не применим к об
letters = ['a', 'b', 'z', 'a']
print(letters)
print('letters.reverse()')
letters.reverse()
print(letters)

print()
nums = [1, 2, 3, 4]
print(nums)
print('nums.reverse()')
nums.reverse()
print(nums)
