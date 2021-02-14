'''
Вещественные числа – это объекты, которые обладают следующими методами:

float.as_integer_ratio() - пара целых чисел, чьё отношение равно этому числу.

float.is_integer() - является ли значение целым числом.

float.hex() - переводит float в hex (шестнадцатеричную систему счисления).

classmethod float.fromhex(s) - float из шестнадцатеричной строки.
'''

print((0.3).as_integer_ratio())
# (5404319552844595, 18014398509481984)

print((0.1).as_integer_ratio())

print(5404319552844595 / 18014398509481984)
# 0.3

from decimal import *

print(Decimal(5404319552844595) / Decimal(18014398509481984))
# Decimal('0.2999999999999999888977697537')

print((3.0).is_integer())
# True
print((3.14).is_integer())
# False

s = (2 + 15. / 16 + 1. / 16 ** 2 + 10. / 16 ** 3) * 2 ** 3
print(s)
# 23.55078125

# Применение обратного преобразования дает другую шестнадцатеричную
# строку, которая, однако, представляет тоже самое число:

print((s).hex())
# '0x1.78d0000000000p+4'

print((1 + 7. / 16 + 8. / 16 ** 2 + 13. / 16 ** 3) * 2 ** 4)
# 23.55078125

# float.hex() - возвращает представление числа в шестнадцатеричной системе счисления:

print((3.141592).hex())
# '0x1.921fafc8b007ap+1'

print((10.01).hex())
# '0x1.4051eb851eb85p+3'

print()
print("float.fromhex('   ')")

print(float.fromhex('0x1.4051eb851eb85p+3'))
# 10.01

# строка может иметь начальные и конечные пробельные символы:
print(float.fromhex('   0x1.921fafc8b007ap+1    '))
# 3.141592

print(float.fromhex('0x0.1p+3'))
# 0.5

print(float.fromhex('0x0.31p+1'))
# 0.3828125

######### доп #########
print(2.78)
print(2.0)
print(2.)  # внимание
print(0.78)
print(.78)  # внимание

list1 = '2.78e-1    2e10    2e+10    2e-10    0e0'.split('   ')
print(list1)
for i in list1:
    print(i)
# list1 = map(float, list)
print(list1)
