students = ['ivan', 'masha', 'sasha']
print(students)
students.append('olga')
print(students)
students += ['nik']
print(students)
# добавляем элементы в списко
students += ['val', 'boris']
print(students)
# добавляем список в список
students += [['val', 'boris']]
print(students)
students += 'igor'
print(students)
# вставка в определенную позицию, количество элементов увеличивается
students.insert(0, 'misha')
print(students)
# извлечение с удалением элемента
print(students.pop(1))
print(students)
print('len(students): ', len(students))
print(students.pop(7))
print(students)
print('len(students): ', len(students))
