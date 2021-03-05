print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("$7")
    else:
        print("$12")

else:
    print("no")
