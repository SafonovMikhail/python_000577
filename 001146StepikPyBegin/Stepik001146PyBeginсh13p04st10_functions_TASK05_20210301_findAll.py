'''
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Следующий программный код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
должен выводить:

[0, 4, 7, 8, 9]
[]
[4]

заготовка:
# объявление функции
def find_all(target, symbol):
    pass

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
'''


# объявление функции
def find_all(target, symbol):
    targ_pos = []
    for i in range(len(target)):
        if target[i]==symbol:
            targ_pos.append(i)
    return targ_pos


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
