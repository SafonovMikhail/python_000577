'''
Наш сайт "товароведов.нет" сформировал заказ для покупателя со следующими данными:
в первой строке наименование заказа,
во второй строке цена - целое число,
в третьей строке дата доставки.

Напиши программу, которая сформирует сообщение для покупателя о сформированном заказе,
в строгом соответствии с представленным шаблоном.

Stepik001132ITclassPyсh01p02st07TASK06_tovar_20200606.py
'''
item = input()
price = int(input())
date1 = input()
print('Ваш товар "', item, '" на сумму', price, 'руб. 00 коп. будет доставлен "', date1, '".')
