'''
Задача «Делаем срезы»
Условие
Дана строка.

Сначала выведите третий символ этой строки.

Во второй строке выведите предпоследний символ этой строки.

В третьей строке выведите первые пять символов этой строки.

В четвертой строке выведите всю строку, кроме последних двух символов.

В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).

В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.

В седьмой строке выведите все символы в обратном порядке.

В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.

В девятой строке выведите длину данной строки.
'''
s = input()
# s = '12345'
print(s[2])  # третий символ
print(s[-2])  # предпоследний символ
print(s[:5])  # первые пять символов
print(s[:-2])  # кроме последних двух (!!!)
print(s[::2])  # четные индексы
print(s[1::2])  # нечетные индексы
print(s[::-1])  # в обратном порядке
print(s[-1::-2])  # через один в обратном порядке
print(len(s))  # длинна строки
