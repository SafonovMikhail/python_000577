'''
Stepik001146PyBeginсh11p04st06TASK05_20210204_lists_methods.py

Google search - 1
На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

Формат входных данных
На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем один поисковый запрос.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречается поисковый запрос.

Примечание. Поиск не должен быть чувствителен к регистру символов.

Sample Input:

5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
язык
Sample Output:

Язык Python прекрасен
C# - отличный язык программирования
язык Python появился 20 февраля 1991
'''
n_str = int(input())
list_strings = []
list_strings_lower = []
for i in range(n_str):
    s = input()
    list_strings.append(s)
    list_strings_lower.append(s.lower())
search_prompt = input()
search_prompt_lower = search_prompt.lower()
# print(list_strings)
# print(list_strings_lower)
# print(search_prompt_lower)
for i in range(len(list_strings_lower)):
    if search_prompt_lower in list_strings_lower[i]:
        print(list_strings[i])
