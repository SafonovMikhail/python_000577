num = input()
if num.isdigit():
    num = int(num)
    if num > 36:
        print("ошибка ввода")
    elif 29 <= num <= 36 and num % 2 != 0:
        print("черный")
    elif 29 <= num <= 36 and num % 2 == 0:
        print("красный")
    elif 19 <= num <= 28 and num % 2 == 0:
        print("черный")
    elif 19 <= num <= 28 and num % 2 != 0:
        print("красный")
    elif 11 <= num <= 18 and num % 2 != 0:
        print("черный")
    elif 11 <= num <= 18 and num % 2 == 0:
        print("красный")
    elif 1 <= num <= 10 and num % 2 == 0:
        print("черный")
    elif 1 <= num <= 10 and num % 2 != 0:
        print("красный")
    else:
        print("зеленый")
else:
    print("ошибка ввода")