'''
Google search - 2 🌶️🌶️
На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем число kk, затем сами поисковые запросы.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.

Sample Input:

5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
2
язык
python
Sample Output:

Язык Python прекрасен
язык Python появился 20 февраля 1991
'''
n_str = int(input())
list_strings = []  # создаем массив строк для поиска
list_strings_lower = []  # создаем параллельный массив в нижнем регистре
list_prompts = []  # создаем список для поисковых запросов
list_prompts_lower = []  # создаем список для поисковых запросов в нижнем регистре
for i in range(n_str):
    s = input()
    list_strings.append(s)  # заполняем список строк
    list_strings_lower.append(s.lower())  # переводим список строк в нижний регистр
k_prompt = int(input())
for i in range(k_prompt):
    sp = input()
    # список запросов сразу создаем в нижнем регистре
    list_prompts_lower.append(sp.lower())
# print(list_strings)
# print(list_strings_lower)
# print(list_prompts_lower)
# flag = 0
# count = 0
# count2 = 0
for i in list_strings_lower:  # перебираем список строк
    flag = 0
    # count += 1
    # print(count)
    for j in list_prompts_lower: # перебираем список запросов
        # count2 += 1
        # print(count2)
        if j in i:
            # print(i)
            # print(j)
            flag += 1
            # print('flag', flag)
        if flag == len(list_prompts_lower):
            # flag = 0
            print(list_strings[list_strings_lower.index(i)])
            continue
# print('flag', flag)
