'''
+ Gooooogle (74)

task_0074_codechick_Google_d20211115.py

[Рекурсия, Строки, Форматирование, Циклы, Легко]

Напишите функцию, которая принимает число number, и возвращает слово Google с количеством букв o, равным number.

Примеры
google(5) => "Gooooogle"
google(0) => "Ggle"
google(2) => "Google"

Примечание

Строка должна начинаться с "G" и заканчиваться на "gle".
На вход подаются только целые числа.

'''


def google(number):
    letters = 'o' * number
    return 'G' + letters + 'gle'


