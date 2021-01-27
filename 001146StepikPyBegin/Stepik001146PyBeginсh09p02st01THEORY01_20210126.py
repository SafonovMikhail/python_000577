s = 'abcdefghij'
print('исходная строка: ', s)  # abcdefghij
print('s[2:5] ', s[2:5])
print('s[0:6] ', s[0:6])
print('s[2:7] ', s[2:7])
print()
print('Срез до конца, от начала')
print('исходная строка: ', s)  # abcdefghij
print('s[2:] ', s[2:])
print('s[:7] ', s[:7])
print('s[:] ', s[:])
print()
print('Отрицательные параметры')
print('исходная строка: ', s)  # abcdefghij
print('s[-9:-4] ', s[-9:-4])  # bcdef
print('s[-3:] ', s[-3:])  # hij
print('s[:-3] ', s[:-3])  # abcdefg
print()
print('Шаг среза')
print('исходная строка: ', s)  # abcdefghij
print('s[1:7:2] ', s[1:7:2])  # bdf
print()
print('Отрицательный шаг среза')
print('исходная строка: ', s)  # abcdefghij
print('s[::-1] ', s[::-1])  # jihgfedcba
print('s[1:7:2] ', s[1:7:2])  # bdf
print('s[3::2] ', s[3::2])  # dfhj
print('s[:7:3] ', s[:7:3])  # adg
print('s[::2] ', s[::2])  # acegi
print('s[::-1] ', s[::-1])  # jihgfedcba
print('s[::-2] ', s[::-2])  # jhfdb
print()
print('Изменение символа строки по индексу')
print('исходная строка: ', s)  # abcdefghij
s = s[:4] + '_X_' + s[5:]
print('результат: ', s)  # abcd_X_fghij
