# переписать без необходимости использовать массив

igrok1 = 0
igrok2 = 0
win = 0
draw = 0
lose = 0
list_choises = ['Камень', 'Ножницы', 'Бумага']

print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 1, введите ваш номер:")
igrok1 = int(input())

print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 2, введите ваш номер:")
igrok2 = int(input())

if igrok1 == 1:
    print('Игрок 1 выбрал Камень')
elif igrok1 == 2:
    print('Игрок 1 выбрал Ножницы')
elif igrok1 == 3:
    print('Игрок 1 выбрал Бумага')
elif igrok2 == 1:
    print('Игрок 2 выбрал Камень')
elif igrok2 == 2:
    print('Игрок 2 выбрал Ножницы')
elif igrok2 == 3:
    print('Игрок 2 выбрал Бумага')