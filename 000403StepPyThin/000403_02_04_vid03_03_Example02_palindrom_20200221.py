s = 'C1GGTGG2C'
# s=input()
r = s[::-1] # создается вторая строка
if s == r:
    print('Y')
else:
    print('N')
'''
Способ не экономный в отношении памяти!
Нужно еще место под аналогичную строку
'''
