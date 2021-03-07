import datetime

print("---------------------------------------")
print("Enter 1 if you want to know about the year (365 or 366 days).")
print("Enter 2 if you want to know about the age group.")
print("Enter 3 if you want to know about the age in seconds.")
print("-------------------------------------")
birth_day = int(input("Your birth day is xx: "))
birth_month = int(input("Your birth month is xx: "))
birth_year = int(input("Your birth year is xxxx: "))
day = int(datetime.date.today().day)
month = int(datetime.date.today().month)
year = int(datetime.date.today().year)
print(f'today: Y: {year}, M: {month}, D: {day}')
number = int(input("Select what you want: "))
if month > birth_month:
    age = year - birth_year
else:
    age = (year - birth_year) - 1

if (number > 0) and (number < 4) and (age >= 0) and (age < 130): # проверка правильности ввода
    if number == 1:  # выбор действия
        if birth_year % 4 != 0:
            print("It is a common year (365 days)")
        else:
            print("It is a leap year (366 days)")
    elif number == 2:  # выбор действия
        print("Your group is ", end="")
        if age < 1:
            print("Baby")
        elif (age >= 1) and (age < 3):
            print("Toddler")
        elif (age >= 3) and (age < 5):
            print("Preschool")
        elif (age >= 5) and (age < 12):
            print("Gradeschooler")
        elif (age >= 12) and (age < 19):
            print("Teen")
        elif age >= 19:
            print("Adult")
    elif number == 3:  # выбор действия
        print("Your age: {} year, {} month, {} day".format(age, abs(month - birth_month), abs(day - birth_day)))
        seconds = ((age * 31536000) + ((month - 1) * 2592000) + ((day - 1) * 86400))
        print("Your age is {} seconds".format(seconds))
else:
    print("Error! Try again.")

