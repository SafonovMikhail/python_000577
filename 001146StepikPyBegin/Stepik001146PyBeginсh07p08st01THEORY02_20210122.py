'''
Операторы break и continue во вложенных циклах
'''
for i in range(3):
    for j in range(3):
        print(i, j)

print('Изменим код, добавив во вложенный цикл условный оператор с оператором break: if i == j')

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

print('Изменим оператор прерывания break на оператор continue: if i == j')

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)