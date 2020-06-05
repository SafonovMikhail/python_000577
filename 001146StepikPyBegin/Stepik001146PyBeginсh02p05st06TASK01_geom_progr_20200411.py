'''
Геометрическая прогрессия
Программа должна вывести n-ый член геометрической прогрессии.
Условие: Stepik001146PyBeginсh02p05st06TASK01_geom_progr
Stepik001146PyBeginсh02p05st06TASK01_geom_progr_20200411.py
'''
b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n - 1))
