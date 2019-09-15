# 000560_02_07_ex01.py

words = ['Hello', 'world', '!']
print(words[0])
print(words[1])
print(words[2])

print("")
print("000560_02_07_task01_lists")
# Каким будет результат вывода
nums = [5, 4, 3, 2, 1]
print(nums[1])
# 4

print("")
print("000560_02_07_ex02_ListsCreate")
# Для создания списка используем квадратные скобки (brackets)
empty_list = []
print(empty_list)
# []

print("")
print("000560_02_07_task02_Lists")
# How many items are in this list?
# [2,]

print("")
print("000560_02_07_ex03_ListsNested")
number = 3
things = ['string', 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
# разобраться с примером использования!!!

print("")
print("000560_02_07_task03_lists")
# Создайте список и выведите на экран его третий элемент
# отсутствовала открывающая скобка
things = [1, 2, 3]
print(things[2])
# обратить внимание, что третий элемент имеет индекс 2(!)

print("")
print("000560_02_07_ex04_ListsSTR")
# Ошибка при вызове несуществующего элемента
# Индексирование строк
str = "Hello world!"
for i in str:
    print(i, end="")
print("\n" + str[6])
print(str[6])
# >>> w

print("")
print("000560_02_07_task04_lists_err")
# Какая строка кода приведет к ошибке?
num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
# print (num[5])
