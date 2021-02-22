'''
11.6 Методы списков. Часть 2 [link]
https://stepik.org/lesson/324754/step/1?discussion=1905163&reply=3485783&unit=307930

Метод insert()
Метод index()
Метод remove()
Метод pop()
Метод reverse()
Метод count()
Метод clear()
Метод sort()
'''

# --------------------------------- #
print('# Метод insert()')
names = ['Gvido', 'Roman', 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)

# --------------------------------- #
print('# Метод index():')
names = ['Gvido', 'Roman', 'Timur']
position = names.index('Timur')
print(position)

names = ['Gvido', 'Roman', 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

# --------------------------------- #
print('# Метод remove()')
food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)

# --------------------------------- #
print('# Метод pop()')
names = ['Gvido', 'Roman', 'Timur']
item = names.pop(1)
print(item)
print(names)

# --------------------------------- #
print('# Метод reverse()')
names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)

# --------------------------------- #
print('# Метод count()')
names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)

# --------------------------------- #
print('# Метод clear()')
names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)

# --------------------------------- #
print('# Метод sort()')
# в THEORY2


