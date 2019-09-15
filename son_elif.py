while True:
    print("Опции:")
    print("Введите 'сумма' для сложения двух чисел")
    print("Введите 'вычетание' для вычетания двух чисел")
    print("Введите 'умножение' для умножения двух чисел")
    print("Введите 'деление' для деления двух чисел")
    print("Введите 'выход' для выхода из программы")
    user_input=input(": ")
    if user_input == "выход":
        break
    elif user_input == "сумма":
        num1 = float(input("Введите число1: "))
        num2 = float(input("Введите число2: "))
        result = str(num1 + num2)
        print("Ответ: " + result)
    elif user_input == "вычетание":
        num1 = float(input("Введите число1: "))
        num2 = float(input("Введите число2: "))
        result = str(num1 - num2)
        print("Ответ: " + result)
    elif user_input == "умножение":
        num1 = float(input("Введите число1: "))
        num2 = float(input("Введите число2: "))
        result = str(num1 * num2)
        print("Ответ: " + result)
    elif user_input == "деление":
        num1 = float(input("Введите число1: "))
        num2 = float(input("Введите число2: "))
        result = str(num1 / num2)
        print("Ответ: " + result)
    else:
        print("Неизвестный ввод.")