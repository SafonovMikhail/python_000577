str1 = input()
# str1 = 'ahahahahaha'
# str1 = 'hh'
print(str1[:str1.find('h')] + str1[str1.rfind('h') + 1:])
'''
Удаление фрагмента
На вход программе подается строка текста, в которой буква «h» встречается
минимум два раза. Напишите программу, которая удаляет из этой строки
первое и последнее вхождение буквы «h», а также все символы,
находящиеся между ними.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

ahahahahaha
Sample Output 1:

aa
Sample Input 2:

hh
Sample Output 2:
'''
