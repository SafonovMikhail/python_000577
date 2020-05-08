s = input()

# [in]
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

# [not] [in]
if '.' not in s:
    print('Введенная строка не содержит символа точки')

# проверка, состоит ли переменная из одного знака из данных
# [aeiou]
if len(s) == 1 and s in 'aeiou':
    print('YES')
else:
    print("NO")