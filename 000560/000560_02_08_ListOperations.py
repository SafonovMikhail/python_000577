print("")
print("000560_02_08_ex01_ListOperations:reassigning")
nums = [5, 4, 3, [2], 1]
print(nums)
nums[2] = 5
print(nums)
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

print("")
print("000560_02_08_task01_listOp")
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
print("nums[3]:",nums[3])



print("")
print("000560_02_08_ex02_ListOperations:AddMultiply")
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



print("")
print("000560_02_08_task02_list")
# переназначьте 2-й элемент и выведите список на экран
nums = [5, 4, 3, [2], 1]
print('nums[1]=22')
nums[1] = 22
print(nums)

print("")
print("000560_02_08_ex03_listBool")
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

print("")
print("000560_02_08_task03_listIfElse")
# Каким будет результат программы?
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

print("")
print("000560_02_08_ex04_listNot")
# Проверка отсутствия элемента в списке
nums = [10, 9, 8, 7, 6, 5]
print(not 4 in nums)
print(4 not in nums)
print(not 9 in nums)
print(9 not in nums)

print("")
print("000560_02_08_task04_listYest")
# Проверка наличия элемента в списке
letters = ['a', 'b', 'z', ]
if 'z' in letters:
    print('Yes')
