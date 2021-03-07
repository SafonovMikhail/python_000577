import random

print("-------Guess my number-------")
print("You need to guess the number picked by enigmatic computer!", "Number is in range from 1 to 10")
magic_number = random.randint(1, 10)
user_number = 0
while user_number != magic_number:
    user_number = int(input("Your number: "))
    if magic_number > user_number:
        print("The magic number is greater than yours!")
    elif magic_number < user_number:
        print("The magic number is less than yours!")
print(f"You guessed it right! Magic number: {magic_number} ")
