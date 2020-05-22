students = ['sasha', 'ivan', 'masha']
students2 = ['sasha', 'ivan', 'masha']
students3 = ['sasha', 'ivan', 'masha']

# Сортировка с изменением исходного списка
print(students)
students.reverse()
print(students)

print("")
print("students2: ", students2)
print("reversed(students2):", reversed(students2))
# обернуть в функцию list()
print("list(reversed(students2)):", list(reversed(students2)))

students4 = reversed(students2)
print("list(students2): ", list(students2))
print("students4: ", students4)

# сортировка без изменения исходного списка
print("")
print(students3)
print(students3[::-1])
