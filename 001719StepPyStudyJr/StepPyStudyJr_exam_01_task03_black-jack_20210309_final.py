import random

# функция создания копии списка карт в числовом эквиваленте
def conv_list(list_cards):
    card_deck_nums = []
    for i in list_cards:
        if str(i).isdigit():
            card_deck_nums.append(i)
        elif i == 'A':
            card_deck_nums.append(11)
        else:
            card_deck_nums.append(10)
    return card_deck_nums

# проверка корректности ввода значений
def correct_input():
    while True:
        add_card = input()
        if add_card == '1' or add_card == '2':
            break
        else:
            print('Введите корректное значение:')
            continue
    return add_card

# проверка состояния игры
def game_condition():
    if count_user == 21 and count_bot == 21:
        print(f'Ничья! Вы: {count_user}, Компьютер: {count_bot}')
        win_comp = 0
        win_user = 0
        return win_comp, win_user
    elif count_user > 21:
        print(f'Вы проиграли! У Вас перебор (очков: {count_user}).')
        win_comp = 1
        win_user = 0
        return win_comp, win_user
    elif count_user == 21:
        print(f'Вы выиграли! У Вас 21.')
        win_comp = 0
        win_user = 1
        return win_comp, win_user
    elif count_bot == 21:
        print(f'Вы проиграли! У компьютера 21.')
        win_comp = 1
        win_user = 0
        return win_comp, win_user
    elif count_user > count_bot:
        print(f'Вы выиграли! Вы: {count_user}, Компьютер: {count_bot}')
        win_comp = 0
        win_user = 1
        return win_comp, win_user
    elif count_user < count_bot:
        print(f'Вы проиграли! Вы: {count_user}, Компьютер: {count_bot}')
        win_comp = 1
        win_user = 0
        return win_comp, win_user
    else:
        print(f'Ничья! Вы: {count_user}, Компьютер: {count_bot}')
        win_comp = 0
        win_user = 0
        return win_comp, win_user


win_comp = 0
win_user = 0
count = 0
count_user = 0
count_bot = 0
result_comp = []
result_user = []
while True:
    # формирование начала игры
    if count != 0:
        print('Хотите еще раз сыграть? \n[yes] - 1 \n[no] - 2')
        select = correct_input()
        if select == '2':
            print('Копьютер выиграл {} раз'.format(result_comp.count(1)))
            print('Пользователь выиграл {} раз'.format(result_user.count(1)))
            print('До встречи!')
            break
    else:
        print('Хотите сыграть? \n[да] - 1 \n[нет] - 2')
        select = correct_input()
        if select == '2':
            print('До встречи!')
            break
    # игра
    while select == '1':
        # ч.01 формирование начального набора карт
        card_deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(card_deck_cards)
        card_deck_nums = conv_list(card_deck_cards)
        count_bot = card_deck_nums.pop() + card_deck_nums.pop()
        count_user = card_deck_nums.pop() + card_deck_nums.pop()
        for i in range(4):
            card_deck_cards.pop()
        print(f'ваш счет: {count_user}')

        # ч.02 выбор дальнейшей игры
        # ввод корректного значения
        while select == '1':
            print('Добавить карту?\n[да] - 1 \n[нет] - 2')
            select = correct_input()
            if select == '1':
                count_user += card_deck_nums.pop()
                added_card = card_deck_cards.pop()
                print(f'Вы выбрали {added_card}.')
                print(f'У Вас {count_user} очков.')
            else:
                result = []
                result.append(game_condition())
                result_comp.append(result[0][0])
                result_user.append(result[0][1])
                break
        count += 1
