num1 = int(input())  # вводим количество строк
list_num = []  # создаем пустой список
for i in range(num1):
    list_num.append(input())  # заполняем список
    # print(len(list_num[i]))
num_letter = int(input()) - 1  # вводим номер буквы
for i in range(len(list_num)):  # пробегаем все элементы списка
    if len(list_num[i]) > num_letter:
        print(list_num[i][num_letter], end='')
        # print(list_num[i])
