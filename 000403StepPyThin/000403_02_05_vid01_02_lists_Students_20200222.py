students = ['ivan', 'masha', 'sasha']
print("students: ", students)
print("len(students): ", len(students))
print("")
# прямая нумерация
print('students[0]:', students[0])
print('students[1]:', students[1])
print('students[2]:', students[2])
print("")
# обратная нумерация
print('students[-3]:', students[-3])
print('students[-2]:', students[-2])
print('students[-1]:', students[-1])
print("")
# левая граница не входит! Выводится второй элемент, но не элемент с индексом 2
print("левая граница не входит!")
print("students[:2]\t", students[:2])
print("")
# вывод списка в обратном порядке
print(students[::-1])
