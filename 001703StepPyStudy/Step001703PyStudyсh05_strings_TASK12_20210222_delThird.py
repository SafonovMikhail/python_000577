'''
Задача «Удалить каждый третий символ»
Условие
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
'''
s = input()
s1 = ''
for i in range(len(s)):
    if i % 3 == 0:
        s1 += s[i + 1:i + 3]
print(s1)

# решение разработчиков
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:  # рационально! Разобрать!
        t = t + s[i]
print(t)
