'''
Задача «Проценты»
Условие
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается
'''
from math import floor, ceil
p = int(input())
x_RUR = int(input())
y_RUKOP = int(input())
sum_kop_begin = x_RUR * 100 + y_RUKOP
sum_kop_end = sum_kop_begin * (1 + p / 100)
# print(int(round(sum_kop_end // 100)), int(round(sum_kop_end % 100)))
print(int(floor(sum_kop_end // 100)), int(ceil((sum_kop_end % 100))))
