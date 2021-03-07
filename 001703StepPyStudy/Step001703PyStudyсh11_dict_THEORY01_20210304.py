'''

'''
# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

print(Capitals)

Countries = ['Russia', 'France', 'USA', 'Russia']

for country in Countries:  # перечисляем ключи (страны)
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if country in Capitals:  # перечисляем занчения
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)

# -----------------------------
print()
print('создание словаря:')
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals1 = dict(Russia='Moscow', Ukraine='Kiev', USA='Washington')
Capitals2 = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals3 = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)
print(Capitals1)
print(Capitals2)
print(Capitals3)

# -----------------------------
print()
print('безопасный способ удаления элементов словаря')
A = {'ab': 'ba', 'aa': 'aa', 'bb': 'bb', 'ba': 'ab'}

key = 'ac'
if key in A:
    del A[key]

try:
    del A[key]
except KeyError:
    print('There is no element with key "' + key + '" in dict')
print(A)

# -----------------------------
print()
print('Перебор элементов словаря(1):')
A = dict(zip('abcdef', list(range(6))))  # строка - спискок ключей
for key in A:
    print(key, A[key])

# -----------------------------
print()
print('Перебор элементов словаря(2):')
A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)
