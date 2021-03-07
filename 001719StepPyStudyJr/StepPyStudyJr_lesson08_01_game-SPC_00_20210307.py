import random

print("-----------------------------------")
print("-------Rock, paper, scissors-------")
print("Welcome to the game!")
print("The game consists of three rounds.")
print("The winner is the one who scores more points.")
print("\t[r] - rock\n\t[s] - scissors\n\t[p] - paper")
player_score = 0
player_select = 0
comp_score = 0
comp_select = 0

print("---------------------------------------")
print("------------[ START GAME ]-------------")
for i in range(3):
    print("\t---------> ROUND № " + str(i + 1) + " <---------")
    comp_select = random.choice("rps")
    while True:
        player_select = input("\tYour choice: ")
        if (player_select == "r") or (player_select == "s") or (player_select == "p"):
            break
        else:
            print("\tError")
    print("\tComputer: " + comp_select)
    if player_select == comp_select:
        print("\tDraw!")
    elif player_select == "r" and comp_select == "s":
        player_score = player_score + 1
        print("\tYou win!")
    elif player_select == "r" and comp_select == "p":
        comp_score = comp_score + 1
        print("\tThe computer wins!")
    elif player_select == "p" and comp_select == "r":
        player_score = player_score + 1
        print("\tYou win!")
    elif player_select == "p" and comp_select == "s":
        comp_score = comp_score + 1
        print("\tThe computer wins!")
    elif player_select == "s" and comp_select == "p":
        player_score = player_score + 1
        print("\tYou win!")
    elif player_select == "s" and comp_select == "r":
        comp_score = comp_score + 1
        print("\tThe computer wins!")
print("-----------------------------------")
print("------------Game Result------------")
if player_score > comp_score:
    print("Congratulations! You win!")
elif player_score < comp_score:
    print("Sorry... The computer wins!")
else:
    print("Draw!")