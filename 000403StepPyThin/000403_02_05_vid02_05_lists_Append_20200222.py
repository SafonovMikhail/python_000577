students = ['ivan', 'masha', 'sasha']
print('students:', students)
students.append('olga')
print("students.append('olga'):", students)
students += ['nik'] # сложение двух списков!
print("students += ['nik']:", students)
# добавляем элементы в списко
students += ['val', 'boris']
print(students)
# добавляем список в список
students += [['val', 'boris']] # список состоит из одного элемента - списка, состоящего, в свою очередь, из двух
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
