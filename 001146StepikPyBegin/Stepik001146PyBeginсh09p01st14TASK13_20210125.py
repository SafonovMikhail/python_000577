str1 = input()
# str1 = 'Вдохновение – это умение приводить себя в рабочее состояние!'
vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
consonant = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
countVow = 0
countCons = 0
for i in str1:
    for j in vowels:
        if i == j:
            countVow += 1
for i in str1:
    for j in consonant:
        if i == j:
            countCons += 1
print(f'Количество гласных букв равно {countVow}')
print(f'Количество согласных букв равно {countCons}')

'''
Гласные и согласные
На вход программе подается одна строка с буквами русского языка. 
Напишите программу, которая определяет количество гласных и согласных букв.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество гласных и согласных букв.

Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) 
и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

Sample Input:

Вдохновение – это умение приводить себя в рабочее состояние!
Sample Output:

Количество гласных букв равно 25
Количество согласных букв равно 24
'''
