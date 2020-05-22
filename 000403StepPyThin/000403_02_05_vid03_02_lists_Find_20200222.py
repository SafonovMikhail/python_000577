students = ['ivan', 'masha', 'sasha']
# проверка наличия элемента
if 'ivan' in students:
    print ('Y')
else:
    print('N')
# проверка отсутствия элемента (синтаксический сахар)
if 'ann' not in students:
    print('Y')
# определение индекса элемента
ind = students.index('sasha')
print(ind)