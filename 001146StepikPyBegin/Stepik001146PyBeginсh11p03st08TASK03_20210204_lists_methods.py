'''
Алфавит
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.
'''
alph = 'abcdefghijklmnopqrstuvwxyz'
abc = []
abc.extend(alph)
for i in range(len(abc)):
    abc[i] = abc[i] * (i+1)
print(abc)
