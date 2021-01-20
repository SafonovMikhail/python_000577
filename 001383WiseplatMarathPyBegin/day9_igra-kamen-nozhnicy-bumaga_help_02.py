import pickle

igrok1="камень"
igrok2="ножницы"

# запись в дамп
game = {"Игрок 1": igrok1, "Игрок 2": igrok2}  # создаем объект
file1 = open("vars_igrokov_help.txt", "wb")  # открываем для побитовой записи
pickle.dump(game, file1)  # записываем в открытый файл данные
file1.close()

# Чтение из дампа
load_file = open("vars_igrokov_help.txt", "rb")  # [rb] побитовое чтение файла
loaded = pickle.load(load_file)  # можем считать объект, который сохранили.
load_file.close()

print(loaded)