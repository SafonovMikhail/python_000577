'''
С помощью функции list() можно из строки получить список ее символов, а с помощью функции join() можно склеить элементы списка, вставляя между ними разделитель.

Что будет выведено в результате выполнения следующего программного кода?

s = 'BEEGEEK'
chars = list(s)
s = '**'.join(chars)
print(s)
'''
s = 'BEEGEEK'
chars = list(s)
print(chars)
s = '**'.join(chars)
print(s)