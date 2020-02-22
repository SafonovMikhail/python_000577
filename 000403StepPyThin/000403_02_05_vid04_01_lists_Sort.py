students = ['sasha', 'ivan', 'masha']
students2 = ['sasha', 'ivan', 'masha']

print('original: ', students)
# список неизменен
sorted_students = sorted(students)
print('sorted(copy): ', sorted_students)
# изменение списка
students2.sort()
print(students2)
