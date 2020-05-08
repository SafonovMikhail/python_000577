string = 'АБ#ВГ'
i = 0
while i < len(string):
    symbol = string[i]
    i = i + 1
    if symbol == '#':
        continue # пропускаем печать символа [#]
    print(symbol)