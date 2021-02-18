'''
За день машина проезжает n километров. Сколько дней нужно,
чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
'''
import math
n_km_per_day = int(input())
m_km_task = int(input())
print(math.ceil(m_km_task / n_km_per_day))
