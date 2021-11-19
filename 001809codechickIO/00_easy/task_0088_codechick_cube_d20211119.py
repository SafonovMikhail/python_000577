'''
Наклейки для кубика Рубика [88]

task_0088_codechick_cube_d20211119.py

[Алгебра, Математика, Легко]

Дан кубик Рубика со стороной n. Верните количество наклеек (квадратов 1x1),
которые потребуются, чтобы покрыть весь кубик.

Картинки кубика Рубика

Для кубика Рубика со стороной 1 потребуется 6 наклеек.
Для кубика Рубика со стороной 2 потребуется 24 наклейки.
Для кубика Рубика со стороной 3 потребуется 54 наклейки.

Примеры
how_many_stickers(1) ➞ 6
how_many_stickers(2) ➞ 24
how_many_stickers(3) ➞ 54

Примечание
 	У кубика Рубика 6 сторон.
 	Длина стороны n — положительное целое число.
 	Количество наклеек — положительное целое число.

'''


def how_many_stickers(n):
    return n * n * 6
