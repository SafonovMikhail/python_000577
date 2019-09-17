# 000560_02_09_ListFunctions.py

print("000560_02_09_ex01_list_append")
# letters[.]append - точка, т.к. это МЕТОД класса из списка
print()
letters = ['a', 'b', 'z', ]
print(letters)
print('letters.append(4)')
letters.append(4)
print(letters)

# 000560_02_09_task01_list_append.py
#
print()
words = ["hello"]
words.append("word")
print(words[1])

# 000560_02_09_ex02_list_len.py
# len и num - метод, а не функция (перед нужным спиком пишется, точка не ставится)
print()
nums = [1, 2, 3, 4, 5, 6, ]
print('len(nums)')
print(len(nums))

# 000560_02_09_task02_list_len.py
#
print()
letters = ['a', 'b', 'c']
print('letters')
print(letters)
print("letters.append('d')")
letters.append('d')
print('len(letters)')
print(len(letters))

# 000560_02_09_ex03_list_insert.py
#
print()
words = ['Python', 'fun']
print('words')
print(words)
print('len(words)')
print(len(words))
print("words.insert('is')")
index = 1
words.insert(index, 'is')
print('len(words)')
print(len(words))
print(words)

# 000560_02_09_task03_list_insert.py
#
print()
nums = [9, 8, 7, 6, 5]
print('len(nums) = ', len(nums))
print(nums)
print('nums.append(4)')
nums.append(4)
print(nums)
print('len(nums) = ', len(nums))
nums.insert(2, 11)
print('nums.insert(2,11)')
print(nums)
print('len(nums) = ', len(nums))

# 000560_02_09_ex04_list_INDEX.py
#
print()
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))  # выдает ошибку, не в списке

# 000560_02_09_task04_list_APPEND_LEN.py
#
print()
list = ['a', 'b', 'z', 'a']
print(list)
print('list.append(z)')
list.append('z')
print(list)
print(len(list))
print()
nums = [1, 2, 3, 4]
print(nums)
print('nums.append(z)')
nums.append('z')
print(nums)
print(len(nums))

# 000560_02_09_ex05_list_MAX.py
#
print()
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print('max(letters)')
print(max(letters))
num = [1, 2, 3, 4, 5, 6]
print()
print(num)
print('max(num)')
print(max(num))

# 000560_02_09_ex06_list_MIN.py
#
print()
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print('min(letters)')
print(min(letters))
num = [1, 2, 3, 4, 5, 6]
print()
print(num)
print('min(num)')
print(min(num))

# 000560_02_09_ex07_list_COUNT.py
#
print()
letters = ['a', 'b', 'z', 'a']
print(letters)
print('letters.count(a)')
print(letters.count('a'))

# 000560_02_09_ex08_list_REMOVE.py
#
print()
letters = ['a', 'b', 'z', 'a']
print(letters)
print('letters.remove(z)')
letters.remove('z')
print(letters)

# 000560_02_09_ex09_list_REVERSE.py
# не применим к об
print()
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
