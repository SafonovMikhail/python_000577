# множественное присваивание
name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name, surname = input("name: "), input("surname: ")
print('Имя:', name, 'Фамилия:', surname)

name1 = 'Timur'
name2 = 'Gvido'
print(name1, name2)
name1, name2 = name2, name1 # обмен значениями переменных
print(name1, name2)
