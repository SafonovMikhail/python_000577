print()

# ----------------------------
print('# Функция с возвратом значения')
print('# задача: цельсии-фаренгейты (функция)')


def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


print()

# ----------------------------
print('# полностью программа:')


# функция перевода градусов Фаренгейта в градусы Цельсия
def convert_to_celsius1(temp):
    result = (5 / 9) * (temp - 32)
    return result


# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius1(temp)
print(celsius)  # градусы Цельсия
print()

# ----------------------------
print('# Использование инструкции return по максимуму')


def convert_to_celsius2(temp):
    return (5 / 9) * (temp - 32)  # в один шаг


print()

# ----------------------------
print('# Использование нескольких return')
print('# стобалльную оценку в пятибалльную')


def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1


# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))

print()

# ----------------------------
print('# переписать с помощью одной инструкции return')


def convert_grade1(grade):
    result = -1
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70:
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1

    return result


# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade1(grade))

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()
