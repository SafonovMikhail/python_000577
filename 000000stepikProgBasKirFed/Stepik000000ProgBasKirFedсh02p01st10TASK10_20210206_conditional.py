'''
Напишите программу, которая переведет название календарного месяца

с русского языка
(Январь, Февраль, Март, Апрель, Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь, Декабрь)

на английский язык
(January, February, March, April, May, June, July, August, September, October, November, December)

Формат входных данных
Строка, содержащая название календарного месяца на русском языке. Первая буква заглавная, остальные - строчные.

Формат выходных данных
Строка, содержащая название календарного месяца на английском языке. Первая буква заглавная, остальные - строчные.

Sample Input:
Апрель
Sample Output:
April
'''
ru_months = input()
if ru_months == 'Январь':
    print('January')
elif ru_months == 'Февраль':
    print('February')
elif ru_months == 'Март':
    print('March')
elif ru_months == 'Апрель':
    print('April')
elif ru_months == 'Май':
    print('May')
elif ru_months == 'Июнь':
    print('June')
elif ru_months == 'Июль':
    print('July')
elif ru_months == 'Август':
    print('August')
elif ru_months == 'Сентябрь':
    print('September')
elif ru_months == 'Октябрь':
    print('October')
elif ru_months == 'Ноябрь':
    print('November')
elif ru_months == 'Декабрь':
    print('December')
