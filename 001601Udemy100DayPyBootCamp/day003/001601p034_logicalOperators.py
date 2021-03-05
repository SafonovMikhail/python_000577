# 001601p034t0334
print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
height = 130

if height >= 120:
    # bill = None
    print("you can ride the rollercoaster!")
    # age = int(input("What is your age? "))
    # age = 15
    age = 49

    if age <= 12:
        bill = 5
        print("$5")
    elif age <= 18:
        bill = 7
        print("$7")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"${bill}")
    else:
        bill = 12
        print("$12")
    # вторая, независимая, проверка!
    wants_photo = input('Do you want photo? (Y/N): ')
    if wants_photo == 'Y':
        # add 3$ to their bill
        # bill = bill + 3
        bill += 3
    print(f"your bill is {bill}")
else:
    print("no")
