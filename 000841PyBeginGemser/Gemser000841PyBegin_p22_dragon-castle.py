import random

# начало игры: 4 двери
print("You are in a dark room in a mysterious castle.")
print("in front of you are four doors. You must choose one.")
playerChoice = input("choose 1, 2, 3 or 4... ")

# выбор дверей (1-4)
if playerChoice == "1":
    print("You find a room full of treasures. You're rich!")
    print("GAME OVER. YOU WIN!")
elif playerChoice == "2":
    print("The door is open an angry ogre hits you with a club.")
    print("GAME OVER. YOU LOSE!")
elif playerChoice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("you can either:")
    print("1) Try to sneak some of the dragons gold.")
    print("2) try to sneak around the drangon to the exit.")
    # выбор внутри двери 3
    dragonschoice = input("type 1 or 2....")
    if dragonschoice == "1":
        print("The dragon wakes up and eats you. You are delicious.")
        print("GAME OVER YOU LOSE")
    elif dragonschoice == "2":
        print("You sneak around the dragon and escape the castle.")
        print("GAME OVER YOU WIN!")
    else:
        print("Sorry, you didn't enter 1 or 2!")

# попали на сфинкса, дверь №4
elif playerChoice == "4":
    print("You enter a room with a sphinx.")
    print("It asks you to guess what number it is thinking of, between 1 and 10.")

    # нужно гарантировать, что ввод будет обрабатываться как целое число (int)
    number = int(input("What number do you choose?"))

    # использование генератора случайных чисел (по условию 1-10, изменил на 1-3)
    if number == random.randint(1, 3):
        print("The sphinx hisses in disappointment. You guessed correctly.")
        print("she must let you go free")
        print("GAME OVER YOU @@@@____WIN____@@@@")
    else:
        print("The sphinx tells you that your guess is incorrect.")
        print("You are now her prisoner forever.")
        print("GAME OVER YOU LOSE")
else:
    print("sorry, you didn't enter 1,2,3 or 4")
print("run the game agian to have another go")
