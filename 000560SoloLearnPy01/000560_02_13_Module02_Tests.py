print()
print("000560_02_test01")
# What is the output of this code?
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
input()

print()
print("000560_02_test02")
# What does this code do?
for i in range(10):
    if not i % 2 == 0:
        print(i + 1)
input()

print()
print("000560_02_test03_looping")
# How many lines will this code print?
while False:
    print('Looping...')
input()

print()
print("000560_02_test04_looping")
# вернуть первый элемент списка, если список содержит четное количество элементов
list = [1, 2, 3, 4]
if len(list) % 2 == 0:
    print(list[0])
input()

print()
print("000560_02_test05_insert")
# что выведет программа?
letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])
input()

print()
print("000560_02_test06_for")
# Используйте цикл for, заполните пропуски так, чтобы перебрать элементы списка и вывести результат.
list = ['x', 'y', 'z']
for i in list:
    print(i, end=" ")
input()
