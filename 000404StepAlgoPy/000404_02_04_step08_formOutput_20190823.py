# 000404_02_04_step08_formOutput.py
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print('{:5d}{:5d}{:5d}'.format(a, b, c))

print('Программа, вычисляющая частное двух чисел. Введите два числа.')
a = int (input ('a: '))
b = int (input ('b: '))
print (a, '/', b, '=', a / b, sep = ' ')

print('Программа, вычисляющая частное двух чисел. Введите два числа.')
a = float (input ('a: '))
b = float (input ('b: '))
print (a, '/', b, '=', a / b, sep = ' ')
# output: 0.01 / 5000.0 = 2e-06

print('Программа, вычисляющая частное двух чисел. Введите два числа.')
e = float(input('e: '))
f = float(input('f: '))
print(e, '/', f, '=', '{:10.17f}'.format(e / f))
print()

name = "Eric"
age = 74
print(F"Hello, {name}. You are {age}.")  # f or F неважно!
# Вывод: 'Hello, Eric. You are 74.'
print()

print(f"{2 * 37}")
# Вывод: '74'
print()

print('def to_lowercase(input):')


def to_lowercase(input):
    return input.lower()


name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
# Вывод: 'eric idle is funny.'
print()

print('name.lower():')
print(f"{name.lower()} is funny.")
# Вывод: 'eric idle is funny.'
print('')


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_Comedian = Comedian('eric', 'Idle', '74')
print(new_Comedian)

print(2, 'a', 8)  # задание позволило обратить внимание на факт вставки пробелов.

print('{:5.2f}'.format(3.1496))  # всего 5 цифр, из них после запятой - 2, при
# этом происходит округление по всем правилам

print('{:5d}'.format(8))

print(2, 'p', 8, sep=', ')
