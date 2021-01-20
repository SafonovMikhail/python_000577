igrok1 = 0
igrok2 = 0
win = 0
draw = 0
lose = 0
list_choises = ['Камень', 'Ножницы', 'Бумага']

print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 1, введите ваш номер:")
igrok1 = int(input())

while 1 < igrok1 > 3:
    print("Введен некорректный номер")
    print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 1, введите ваш номер:")
    igrok1 = int(input())

if igrok1 == 1:
    print('Игрок 1 выбрал %s' % list_choises[1 - igrok1])
elif igrok1 == 2:
    print('Игрок 1 выбрал %s' % list_choises[1 - igrok1])
elif igrok1 == 3:
    print('Игрок 1 выбрал %s' % list_choises[1 - igrok1])

print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 2, введите ваш номер:")
igrok2 = int(input())
while 1 < igrok2 > 3:
    for i in range(3):
        print("Введен некорректный номер")
        print("(Камень - 1, Ножницы - 2, Бумага - 3) Игрок 1, введите ваш номер:")
        igrok2 = int(input())
    print("Вы три раза ввели неверное число. Вы проиграли!")

    break

if igrok2 == 1:
    print('Игрок 2 выбрал %s' % list_choises[1 - igrok2])
elif igrok2 == 2:
    print('Игрок 2 выбрал %s' % list_choises[1 - igrok2])
elif igrok2 == 3:
    print('Игрок 2 выбрал %s' % list_choises[1 - igrok2])
