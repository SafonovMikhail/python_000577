year = 2010
sum1 = '10k'
currency = 'Bitcoin'
quantity = 'two'
print(f'In {year}, someone paid {sum1} {currency} for {quantity} pizzas.')
'''
Дополните приведенный код, используя форматирование строк с помощью 
метода format, так чтобы он вывел текст: 

«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).

представленный код:

s = 'In {0}, someone paid {1} {2} for two pizzas.'

print()

'''

s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(2010,'10k','Bitcoin')
print(s)