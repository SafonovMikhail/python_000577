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

# print("Игрок 1 выбрал номер:", igrok1, "Игрок 2 выбрал номер:", igrok2)
print('Игрок 1 выбрал:', list_choises[igrok1 - 1], 'Игрок 2 выбрал:', list_choises[igrok2 - 1])

# Вычитаем 1, потому, что индекс элементов начинается с нуля