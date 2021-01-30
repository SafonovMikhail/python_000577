str1 = input()
# str1 = 'ahahahahaha'
# str1 = 'hh'
str2 = ''
index_h_left = str1.find('h')
index_h_right = str1.rfind('h')
for i in range(len(str1)):
    if index_h_left <= i <= index_h_right:
        continue
    else:
        str2 += str1[i]
print(str2)
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
