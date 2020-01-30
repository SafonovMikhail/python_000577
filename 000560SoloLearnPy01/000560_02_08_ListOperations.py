print("")
print("000560_02_08_ex01_ListOperations:reassigning")
nums = [5, 4, 3, [2], 1]
print(nums)
nums[2] = 5
print(nums)
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

# print("")
print("\n000560_02_08_task01_listOp")
nums = [5, 4, 3, [2], 1]
print(nums)
nums[3] = nums[1]
print('nums[3] = nums[1]')
print(nums)
print('nums[3]:', nums[3])
# каков будет результат вычисления
nums = [1, 2, 3, 4, 5]
print(nums)
nums[3] = nums[1]
print('nums[3] = nums[1]')
print(nums)
print("nums[3]:", nums[3])

# print("")
print("\n000560_02_08_ex02_ListOperations:AddMultiply")
nums = [5, 4, 3, [2], 1]
print('nums')
print(nums)
print('nums + [4,5,6]')
print(nums + [4, 5, 6])
print('nums * 3')
print(nums * 3)
print("var.02")
nums = [1, 2, 3]
print(nums)
print("nums + [4, 5, 6]")
print(nums + [4, 5, 6])
print(nums * 3)
# рассмотреть различные варианты умножения элементов списка:
# поэлементно, каждый элемент по 3 раза

# print("")
print("\n000560_02_08_task02_list")
# переназначьте 2-й элемент и выведите список на экран
nums = [5, 4, 3, [2], 1]
print('nums[1]=22')
nums[1] = 22
print(nums)

print("\n000560_02_08_ex03_ListOp")
# Проверка на наличие элемента в списке
words = ['spam', 'egg', 'spam', 'sausage']
print("words[]")
print(words)
print("'spam' in words")
print('spam' in words)
print("'egg' in words")
print('egg' in words)
print("'tomato' in words")
print('tomato' in words)

print('\n000560_02_08_ex03-01_ListOp:"hello" in "hello world"')
print("hello" in "hello world")
'''
because every string is treated as a list.
and "hello" is a substring of "hello world"
'''

print('\n000560_02_08_ex03-02_ListOp:"elements in lists"')
x = ["eggs", " spam"]
print("pam" in x)
# False
print("pam" in x[1])
# True

print('\n000560_02_08_ex03-03_ListOp:\"example \'elements in list\'"')
A = 3
print("A:", A)
B = "s"
print("B:", B)
C = [A, B, 1, "Hello World"]
print("C:", C)
print("1 in C:", 1 in C)  # True
print("A in C:", A in C)  # True
print('"s" in C:', "s" in C)  # True
print("B in C:", B in C)  # True
print('3 in C:', 3 in C)  # True
print('"H" in C:', "H" in C)  # False
print('"Hello" in C:', "Hello" in C)  # False
print('"Hello World" in C', "Hello World" in C)  # True

# print()
print('\n000560_02_08_ex03-03_ListOp:"example \'elements in list\' 02"')
tools = ["wrench", "putty knife", "jigsaw", ["nut", "bolt", "washer"], "hacksaw"]
print("washer" in tools[3])
print("washer" in tools)
print(tools[2][3:5] in tools[4])
print(tools[2][3:5] in tools)

# print("")
print("\n000560_02_08_task03_listIfElse")
# Каким будет результат программы?
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

# print("")
print("\n000560_02_08_ex04_listNot")
# Проверка отсутствия элемента в списке
nums = [10, 9, 8, 7, 6, 5]
print(not 4 in nums)
print(4 not in nums)
print(not 9 in nums)
print(9 not in nums)

# print("")
print("\n000560_02_08_task04_listYest")
# Проверка наличия элемента в списке
letters = ['a', 'b', 'z', ]
if 'z' in letters:
    print('Yes')
