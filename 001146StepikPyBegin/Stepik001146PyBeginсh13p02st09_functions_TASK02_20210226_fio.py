'''
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

Sample Input 1:

Александр
Пушкин
Сергеевич
Sample Output 1:

ПАС
Sample Input 2:

тимур
Гуев
ахсарбекович
Sample Output 2:

ГТА

заготовка:
# объявление функции
def print_fio(name, surname, patronymic):
    pass

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

'''


def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep='')


name = input()
surname = input()
patronymic = input()

print_fio(name.title(), surname.title(), patronymic.title())


# Дарья Смирнова
# https://stepik.org/lesson/333525/step/9?discussion=1632598&thread=solutions&unit=316953

# объявление функции
def print_fio(name, surname, patronymic):
    print((surname[0] + name[0] + patronymic[0]).upper())
    pass


# считываем данные
name, surname, patronymic = input(), input(), input(),

# вызываем функцию
print_fio(name, surname, patronymic)

print()


# -------------------------------------------

# Юрий Токмань
# https://stepik.org/lesson/333525/step/9?discussion=1890247&thread=solutions&unit=316953
# объявление функции
def print_fio(name, surname, patronymic):
    [print(m[0].upper(), end='') for m in [surname, name, patronymic]]


# считываем данные
name, surname, patronymic = input(), input(), input(),
# вызываем функцию
print_fio(name, surname, patronymic)

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------

print()
# -------------------------------------------
