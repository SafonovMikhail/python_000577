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


# начальный набор карт (по 2 карты)
def init(list_num, list_cards):
    count_you = card_deck_nums.pop() + card_deck_nums.pop()
    count_bot = card_deck_nums.pop() + card_deck_nums.pop()
    for i in range(4):
        card_deck_cards.pop()
    print(f'Your score is {count_you}')
    print(len(card_deck_nums))
    print(len(card_deck_cards))
    return count_you, count_bot


# Отображение результата игры
def print_win(y, b):
    print(f'you won {y} times, bot won {b} times')


print("===================================")
print("***********[ Black Jack ]**********")
print("-----------------------------------")
# card_deck_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
card_deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
card_deck_nums = []
count = 0
game_exit = 0
count_you = 0
count_bot = 0
win_you = 0
win_bot = 0
while True:
    # формирование предложения к игре в зависимости от начальных условий
    # игра уже была или нет
    if game_exit == 1:
        break
    elif count == 0:
        print("Would you like to start a new game?\n\t[y] - yes\n\t[n] - no\n")
        select_play = input().lower()
    else:
        print("\nWould you like to play one more time?\n\t[y] - yes\n\t[n] - no\n")
        select_play = input().lower()

    # проверяем корректность ввода
    while True:
        if select_play == "y" or select_play == "n":
            break
        else:
            select_play = input('введите корректное значение ("y" или "n"): ').lower()
            # print(select)
            continue

    # начальные условия
    card_deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

    # тасуем колоду
    random.shuffle(card_deck_cards)

    # формируем второй список, содержащий численные эквиваленты карт
    card_deck_nums = conv_list(card_deck_cards)

    # набираем из колоды по 2 карты и выводим сумму очков пользователя
    count_you, count_bot = init(card_deck_nums, card_deck_cards)

    # код игры
    while True:
        if select_play == 'n' and count == 0:
            print('See you ))')
            game_exit == 1
            break
        else:
            print(print_win(win_you, win_bot))
            game_exit = 1
            break

        select_card = input("\nAdd a card? \n\t[y] - yes\n\t[n] - no \n")
        if select_card == "y":
            current_card = card_deck_cards.pop()
            print(f"Your card is: {current_card}")
            count_you += card_deck_nums.pop()

            # проверяем условия выигрыша/проигрыша
            if count_you > 21:
                print("Sorry... You lose! (you scored over 21)")
                win_bot += 1
                print(f"Your score: {count_you}")
                break
            elif count_you == 21:
                print("Congratulations! You win! (you scored 21)")
                win_you += 1
                print(f"Total score: {count_you}")
                break
            elif count_bot > 21:
                print(f"Congratulations! You win! Bot's score: {count_bot}")
                win_you += 1
                print(f"Your score: {count_you}")
            else:
                print(f"Your score: {count_you}")
        if select_card == "n":
            print(f"Stop. Your score: {count_you}")
            if count_you > count_bot:
                print(f"Stop. You win!!! Your score: {count_you}, Bot's score: {count_bot}")
                win_you += 1
                # print(print_win(win_you, win_bot))
            elif count_you == count_bot:
                print(f"Stop. Draw!!! Your score: {count_you}, Bot's score: {count_bot}")
                # print(print_win(win_you, win_bot))
            else:
                print(f"Stop. You loose!!! Your score: {count_you}, Bot's score: {count_bot}")
                win_bot += 1
                # print(print_win(win_you, win_bot))

            print("\n-------------Game Over-------------")
            count += 1
            break
