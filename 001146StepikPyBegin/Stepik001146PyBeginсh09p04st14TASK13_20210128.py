str1 = input()
count_f = 0
first_index = None
for i in range(len(str1)):
    if str1[i] == 'f':
        count_f += 1
if count_f == 1:
    print(str1.find('f'))
if count_f >= 2:
    print(str1.find('f'), str1.rfind('f'))
if count_f == 0:
    print('NO')
'''
Первое и последнее вхождение
На вход программе подается строка текста. 
Если в этой строке буква «f»
встречается только один раз, выведите её индекс. 

Если она встречается
два и более раз, выведите индекс её первого и последнего вхождения на
одной строке, разделенных символом пробела. Если буква «f» в данной 
строке не встречается, следует вывести «NO».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

abcdefg
Sample Output 1:

5
Sample Input 2:

abcdefgfhfabc
Sample Output 2:

5 9
Sample Input 3:

abcd
Sample Output 3:

NO
'''
