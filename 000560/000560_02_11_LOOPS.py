print()
# выводим на печать все слова в списке
print("000560_02_11_ex01_loop_WHILE")
words = ['hello', 'words', 'spam', 'eggs']
counter = 0  # объявляем переменную-счетчик
max_index = len(words) - 1  # максимальный индекс в списке
while counter <= max_index:
    word = words[counter]  # перебор всех слов
    print(word, '!')
    counter = counter + 1

print()
# выводим на печать все слова в списке, без счетчика
print("000560_02_11_ex02_loop_FOR")
words = ['hello', 'words', 'spam', 'eggs']
for i in words:
    print(i, '!')

print()
print("000560_02_11_task02_loop_FOR")
words = ['hello', 'words', 'spam', 'eggs']
for i in words:
    print(i)

print()
# выполнение кода определенное количество раз
print("000560_02_11_ex03_loop_FOR")
for i in range(5):
    print('Hi!')

print()
# выводить только четные числа в заданном диапазоне
print("000560_02_11_task03_loop_FOR")
for i in range(0, 20, 2):
    print(i)
# (?) как полученные результаты преобразовать в массив или список
